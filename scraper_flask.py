#!/usr/bin/env python3
from flask import Flask, request, jsonify, Response
import asyncio
import os
import time
import threading
from queue import Queue
from scraper import WebCrawler  # Import the WebCrawler class from scraper.py

app = Flask(__name__)
progress_queue = Queue()
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

    crawler = WebCrawler(base_url, output_dir)
    crawler_id = id(crawler)
    active_crawlers[crawler_id] = crawler

    # Clear progress queue
    while not progress_queue.empty():
        progress_queue.get()

    # Run crawl_site in a separate thread to avoid blocking Flask
    def run_crawl():
        try:
            # Create a new event loop for this thread
            loop = asyncio.new_event_loop()
            asyncio.set_event_loop(loop)
            loop.run_until_complete(crawler.crawl_site())
            progress_queue.put("Crawl complete.")
            progress_queue.put("DONE")
        except Exception as e:
            progress_queue.put(f"Error: {e}")
        finally:
            if crawler_id in active_crawlers:
                del active_crawlers[crawler_id]

    threading.Thread(target=run_crawl).start()

    return jsonify({'status': 'success', 'message': 'Crawl started', 'crawler_id': crawler_id})

@app.route('/stream_progress')
def stream_progress():
    def generate():
        while True:
            if not progress_queue.empty():
                message = progress_queue.get()
                yield f"data: {message}\n\n"
                if message == "DONE":
                    break
            else:
                time.sleep(0.1)
    return Response(generate(), mimetype='text/event-stream')

@app.route('/')
def home():
    return '''
    <!DOCTYPE html>
    <html>
      <head>
          <title>Scraper Interface</title>
          <style>
              body { font-family: Arial, sans-serif; max-width: 800px; margin: auto; padding: 20px; }
              input[type=text] { width: 100%; padding: 8px; margin-bottom: 10px; }
              button { padding: 10px; margin: 5px; }
              #progress { background: #f0f0f0; padding: 10px; border: 1px solid #ccc; height: 300px; overflow-y: auto; }
          </style>
      </head>
      <body>
          <h1>Scraper Interface</h1>
          <input type="text" id="url" placeholder="Enter URL to crawl">
          <input type="text" id="output_dir" placeholder="Output directory (default: crawled_data)" value="crawled_data">
          <button onclick="startCrawl()">Start Crawl</button>
          <button onclick="stopCrawl()">Stop Crawl</button>
          <div id="progress"></div>
          <script>
            var currentCrawlerId = null;
            var eventSource = null;
            function startCrawl() {
              var url = document.getElementById('url').value;
              var output_dir = document.getElementById('output_dir').value;
              if (!url) { alert('URL is required'); return; }
              document.getElementById('progress').innerHTML = '';
              if (eventSource) { eventSource.close(); }
              eventSource = new EventSource('/stream_progress');
              eventSource.onmessage = function(event) {
                var progressDiv = document.getElementById('progress');
                progressDiv.innerHTML += event.data + '<br>';
                progressDiv.scrollTop = progressDiv.scrollHeight;
              };
              fetch('/crawl', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({url: url, output_dir: output_dir})
              })
              .then(response => response.json())
              .then(data => { currentCrawlerId = data.crawler_id; });
            }
            function stopCrawl() {
              if (!currentCrawlerId) return;
              fetch('/stop_crawl', {
                method: 'POST',
                headers: { 'Content-Type': 'application/json' },
                body: JSON.stringify({crawler_id: currentCrawlerId})
              })
              .then(response => response.json())
              .then(data => { console.log(data); });
            }
          </script>
      </body>
    </html>
    '''

if __name__ == '__main__':
    app.run(debug=True) 