from flask import Flask, request, jsonify, Response
import asyncio
import os
from pathlib import Path
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode
from bs4 import BeautifulSoup
import aiohttp
import re
from urllib.parse import urljoin, urlparse
import time
from queue import Queue

app = Flask(__name__)
progress_queue = Queue()  # Add this line

class WebCrawler:
    def __init__(self, base_url, output_dir="crawled_data"):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited_urls = set()
        self.output_dir = output_dir
        self.should_stop = False
        self.browser_config = BrowserConfig(
            headless=True,
            verbose=True
        )
        self.run_config = CrawlerRunConfig(
            cache_mode=CacheMode.ENABLED,
        )
        
        # Create output directory if it doesn't exist
        os.makedirs(output_dir, exist_ok=True)

    def stop_crawl(self):
        """Stop the crawling process"""
        self.should_stop = True

    async def get_all_links(self, url):
        """Extract all links from a webpage that belong to the same domain"""
        try:
            timeout = aiohttp.ClientTimeout(total=10)  # 10 second timeout for link extraction
            async with aiohttp.ClientSession(timeout=timeout) as session:
                async with session.get(url) as response:
                    if response.status != 200:
                        return set()
                    
                    html = await response.text()
                    soup = BeautifulSoup(html, 'html.parser')
                    links = soup.find_all('a', href=True)
                    
                    valid_links = set()
                    for link in links:
                        href = link['href']
                        full_url = urljoin(url, href)
                        
                        # Remove anchor fragments and normalize URL
                        parsed_url = urlparse(full_url)
                        # Skip certain file types and patterns
                        if any(ext in parsed_url.path.lower() for ext in ['.pdf', '.jpg', '.png', '.gif']):
                            continue
                        if any(pattern in parsed_url.path.lower() for pattern in ['/static/', '/assets/']):
                            continue
                            
                        normalized_url = parsed_url._replace(
                            fragment='',  # Remove anchor fragments
                            query=''      # Remove query parameters
                        ).geturl()
                        
                        # Only include links from the same domain
                        if urlparse(normalized_url).netloc == self.domain:
                            valid_links.add(normalized_url)
                    
                    return valid_links
        except Exception as e:
            print(f"Error getting links from {url}: {str(e)}")
            return set()

    def sanitize_filename(self, url):
        """Convert URL to a valid filename"""
        # Remove protocol and domain
        filename = url.replace(f"https://{self.domain}", "").replace(f"http://{self.domain}", "")
        # Replace invalid characters
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        # Remove leading/trailing underscores and spaces
        filename = filename.strip('_').strip()
        # Add .md extension
        if not filename:
            filename = "index"
        return f"{filename}.md"

    async def crawl_page(self, url):
        """Crawl a single page and save its markdown content"""
        try:
            # Check if page already exists
            filename = self.sanitize_filename(url)
            filepath = os.path.join(self.output_dir, filename)
            
            # Skip if file already exists
            if os.path.exists(filepath):
                return None
                
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                result = await crawler.arun(
                    url=url,
                    config=self.run_config
                )
                
                # Add metadata at the top of the file
                metadata = f"""---
url: {url}
title: {result.title if hasattr(result, 'title') else 'Untitled'}
date_crawled: {result.timestamp if hasattr(result, 'timestamp') else ''}
---

"""
                
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(metadata + result.markdown)
                
                return filepath
        except Exception as e:
            print(f"Error crawling {url}: {str(e)}")
            return None

    def get_existing_pages(self):
        """Get list of already crawled pages from the output directory"""
        existing_pages = set()
        if os.path.exists(self.output_dir):
            for filename in os.listdir(self.output_dir):
                if filename.endswith('.md'):
                    filepath = os.path.join(self.output_dir, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            # Skip the first line (---)
                            f.readline()
                            # Read until we find the URL
                            for line in f:
                                if line.startswith('url:'):
                                    url = line[4:].strip()
                                    existing_pages.add(url)
                                    break
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")
        return existing_pages

    async def crawl_site(self):
        """Crawl the site continuously in batches, skipping already crawled pages"""
        self.should_stop = False
        crawled_files = []
        batch_size = 10  # Process 10 pages concurrently
        pages_crawled = 0
        
        # Get already crawled pages
        existing_pages = self.get_existing_pages()
        progress_queue.put(f"Found {len(existing_pages)} already crawled pages")
        
        # Start with base URL
        to_visit = {self.base_url}
        self.visited_urls = existing_pages.copy()  # Initialize with existing pages

        # Get new URLs from existing pages to ensure we find new content
        progress_queue.put("Checking existing pages for new links...")
        for url in existing_pages:
            try:
                new_links = await self.get_all_links(url)
                to_visit.update(new_links - self.visited_urls)
            except Exception as e:
                progress_queue.put(f"Error getting links from {url}: {e}")

        progress_queue.put(f"Found {len(to_visit)} new pages to check")

        while to_visit and not self.should_stop:
            current_batch = set()
            while len(current_batch) < batch_size and to_visit:
                url = to_visit.pop()
                if url not in self.visited_urls:
                    current_batch.add(url)
                    self.visited_urls.add(url)

            if not current_batch:
                break  # No more new pages to crawl

            progress_queue.put(f"Crawling batch of {len(current_batch)} pages...")
            progress_queue.put(f"New pages in this run: {pages_crawled}")
            progress_queue.put(f"Total pages (including existing): {len(existing_pages) + pages_crawled}")
            
            try:
                crawl_tasks = [self.crawl_page(url) for url in current_batch]
                batch_results = await asyncio.gather(*crawl_tasks, return_exceptions=True)

                for result in batch_results:
                    if isinstance(result, str):  # Successful filepath
                        crawled_files.append(result)
                        pages_crawled += 1
                
                # Get new URLs to visit from the current batch
                for url in current_batch:
                    try:
                        new_links = await self.get_all_links(url)
                        to_visit.update(new_links - self.visited_urls)
                    except Exception as e:
                        progress_queue.put(f"Error getting links from {url}: {e}")

            except Exception as e:
                progress_queue.put(f"Error in batch: {str(e)}")
                continue

        # Double-check final count from filesystem
        final_existing_pages = self.get_existing_pages()
        total_pages = len(final_existing_pages)
        
        if pages_crawled == 0:
            progress_queue.put("No new pages found to crawl")
        progress_queue.put(f"Crawl complete. New pages added in this run: {pages_crawled}")
        progress_queue.put(f"Total pages in folder: {total_pages}")
        progress_queue.put("DONE")
        return crawled_files, total_pages

# Add a global dictionary to store crawler instances
active_crawlers = {}

@app.route('/stop_crawl', methods=['POST'])
def stop_crawl():
    data = request.get_json()
    crawler_id = data.get('crawler_id')
    
    if crawler_id in active_crawlers:
        active_crawlers[crawler_id].stop_crawl()
        return jsonify({'status': 'success', 'message': 'Crawl stopping...'})
    return jsonify({'status': 'error', 'message': 'Crawler not found'}), 404

@app.route('/crawl', methods=['POST'])
def crawl():
    data = request.get_json()
    if not data or 'url' not in data:
        return jsonify({'error': 'URL is required'}), 400

    base_url = data['url']
    output_dir = data.get('output_dir', 'crawled_data')

    try:
        crawler = WebCrawler(base_url, output_dir)
        global currentCrawlerId
        currentCrawlerId = id(crawler)  # Set the current crawler ID
        active_crawlers[currentCrawlerId] = crawler
        
        # Clear any existing messages in the queue
        while not progress_queue.empty():
            progress_queue.get()
            
        crawled_files, total_pages = asyncio.run(crawler.crawl_site())
        
        # Clean up
        del active_crawlers[currentCrawlerId]
        
        return jsonify({
            'status': 'success',
            'message': f'Successfully crawled {len(crawled_files)} out of {total_pages} pages',
            'crawled_files': crawled_files,
            'output_directory': output_dir,
            'total_pages': total_pages,
            'stopped': crawler.should_stop
        })

    except Exception as e:
        return jsonify({
            'status': 'error',
            'message': str(e)
        }), 500

@app.route('/stream_progress')
def stream_progress():
    def generate():
        while True:
            # Check for new messages in the progress queue
            if not progress_queue.empty():
                message = progress_queue.get()
                if message == "DONE":
                    break
                yield f"data: {message}\n\n"
            else:
                time.sleep(0.1)
    return Response(generate(), mimetype='text/event-stream')

@app.route('/', methods=['GET'])
def home():
    return '''
    <!DOCTYPE html>
    <html>
    <head>
        <title>Web Crawler Interface</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                max-width: 800px;
                margin: 0 auto;
                padding: 20px;
            }
            .form-group {
                margin-bottom: 15px;
            }
            label {
                display: block;
                margin-bottom: 5px;
            }
            input[type="text"] {
                width: 100%;
                padding: 8px;
                margin-bottom: 10px;
            }
            button {
                background-color: #4CAF50;
                color: white;
                padding: 10px 15px;
                border: none;
                border-radius: 4px;
                cursor: pointer;
            }
            button:hover {
                background-color: #45a049;
            }
            #result {
                margin-top: 20px;
                padding: 10px;
                border: 1px solid #ddd;
                display: none;
            }
            .button-group {
                display: flex;
                gap: 10px;
            }
            #stopButton {
                background-color: #dc3545;
                display: none;
            }
            #stopButton:hover {
                background-color: #c82333;
            }
            #progress {
                font-family: monospace;
                white-space: pre-wrap;
                background-color: #f8f9fa;
                padding: 10px;
                border: 1px solid #ddd;
                margin-top: 10px;
                max-height: 300px;
                overflow-y: auto;
            }
        </style>
    </head>
    <body>
        <h1>Web Crawler Interface</h1>
        <div class="form-group">
            <label for="url">Website URL to Crawl:</label>
            <input type="text" id="url" placeholder="https://example.com" required>
        </div>
        <div class="form-group">
            <label for="output_dir">Output Directory:</label>
            <input type="text" id="output_dir" placeholder="crawled_data" value="crawled_data">
        </div>
        <div class="button-group">
            <button onclick="startCrawl()" id="crawlButton">Start Crawling</button>
            <button onclick="stopCrawl()" id="stopButton">Stop Crawling</button>
        </div>
        <div id="progress"></div>
        <div id="result"></div>

        <script>
        let currentCrawlerId = null;
        let eventSource = null;

        function setupEventSource() {
            const progressDiv = document.getElementById('progress');
            if (eventSource) {
                eventSource.close();
            }
            eventSource = new EventSource('/stream_progress');
            
            eventSource.onmessage = function(event) {
                console.log('Received:', event.data);  // Add debugging
                if (event.data === "DONE") {
                    eventSource.close();
                } else {
                    progressDiv.innerHTML += event.data + '\\n';
                    progressDiv.scrollTop = progressDiv.scrollHeight;
                }
            };

            eventSource.onerror = function(error) {
                console.error('EventSource error:', error);
            };
        }

        async function stopCrawl() {
            if (!currentCrawlerId) return;
            
            try {
                const response = await fetch('/stop_crawl', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        crawler_id: currentCrawlerId
                    })
                });

                const data = await response.json();
                if (data.status === 'success') {
                    document.getElementById('progress').innerHTML += 'Stopping crawler...\\n';
                }
            } catch (error) {
                console.error('Error stopping crawler:', error);
            }
        }

        async function startCrawl() {
            const url = document.getElementById('url').value;
            const output_dir = document.getElementById('output_dir').value;
            const resultDiv = document.getElementById('result');
            const progressDiv = document.getElementById('progress');
            const crawlButton = document.getElementById('crawlButton');
            const stopButton = document.getElementById('stopButton');
            
            if (!url) {
                alert('Please enter a URL');
                return;
            }

            // Clear previous progress
            progressDiv.innerHTML = '';
            resultDiv.style.display = 'block';
            crawlButton.disabled = true;
            stopButton.style.display = 'block';

            // Setup event source for progress updates
            setupEventSource();

            try {
                const response = await fetch('/crawl', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                    },
                    body: JSON.stringify({
                        url: url,
                        output_dir: output_dir
                    })
                });

                const data = await response.json();
                if (data.status === 'success') {
                    const stoppedMessage = data.stopped ? '<p>Crawl was stopped by user</p>' : '';
                    resultDiv.innerHTML = `
                        <h3>Crawl Complete!</h3>
                        ${stoppedMessage}
                        <p>${data.message}</p>
                        <p>Files saved in: ${data.output_directory}</p>
                        <p>Total pages found: ${data.total_pages}</p>
                        <p>Pages successfully crawled: ${data.crawled_files.length}</p>
                    `;
                } else {
                    resultDiv.innerHTML = `Error: ${data.message}`;
                }
            } catch (error) {
                resultDiv.innerHTML = `Error: ${error.message}`;
            } finally {
                if (eventSource) {
                    eventSource.close();
                }
                crawlButton.disabled = false;
                stopButton.style.display = 'none';
                currentCrawlerId = null;
            }
        }
        </script>
    </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True) 