#!/usr/bin/env python3
import asyncio
import os
import re
import sys
from urllib.parse import urljoin, urlparse
import aiohttp
from bs4 import BeautifulSoup
from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig, CacheMode


class WebCrawler:
    def __init__(self, base_url, output_dir="crawled_data"):
        self.base_url = base_url
        self.domain = urlparse(base_url).netloc
        self.visited_urls = set()
        self.output_dir = output_dir
        self.should_stop = False
        self.browser_config = BrowserConfig(headless=True, verbose=True)
        self.run_config = CrawlerRunConfig(cache_mode=CacheMode.ENABLED)
        os.makedirs(output_dir, exist_ok=True)

    def stop_crawl(self):
        self.should_stop = True

    async def get_all_links(self, url):
        try:
            timeout = aiohttp.ClientTimeout(total=10)
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
                        parsed_url = urlparse(full_url)
                        if any(ext in parsed_url.path.lower() for ext in ['.pdf', '.jpg', '.png', '.gif']):
                            continue
                        if any(pattern in parsed_url.path.lower() for pattern in ['/static/', '/assets/']):
                            continue
                        normalized_url = parsed_url._replace(fragment='', query='').geturl()
                        if urlparse(normalized_url).netloc == self.domain:
                            valid_links.add(normalized_url)
                    return valid_links
        except Exception as e:
            print(f"Error getting links from {url}: {e}")
            return set()

    def sanitize_filename(self, url):
        filename = url.replace(f"https://{self.domain}", "").replace(f"http://{self.domain}", "")
        filename = re.sub(r'[<>:"/\\|?*]', '_', filename)
        filename = filename.strip('_').strip()
        if not filename:
            filename = "index"
        return f"{filename}.md"

    async def crawl_page(self, url):
        try:
            filename = self.sanitize_filename(url)
            filepath = os.path.join(self.output_dir, filename)
            if os.path.exists(filepath):
                return None
            async with AsyncWebCrawler(config=self.browser_config) as crawler:
                result = await crawler.arun(url=url, config=self.run_config)
                metadata = f"---\nurl: {url}\ntitle: {result.title if hasattr(result, 'title') else 'Untitled'}\ndate_crawled: {result.timestamp if hasattr(result, 'timestamp') else ''}\n---\n\n"
                content = metadata + result.markdown
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(content)
                print(f"Saved: {filepath}")
                return filepath
        except Exception as e:
            print(f"Error crawling {url}: {e}")
            return None

    def get_existing_pages(self):
        existing_pages = set()
        if os.path.exists(self.output_dir):
            for filename in os.listdir(self.output_dir):
                if filename.endswith('.md'):
                    filepath = os.path.join(self.output_dir, filename)
                    try:
                        with open(filepath, 'r', encoding='utf-8') as f:
                            f.readline()  # Skip first line (---)
                            for line in f:
                                if line.startswith('url:'):
                                    url = line[4:].strip()
                                    existing_pages.add(url)
                                    break
                    except Exception as e:
                        print(f"Error reading {filepath}: {e}")
        return existing_pages

    async def crawl_site(self):
        self.should_stop = False
        crawled_files = []
        batch_size = 10
        pages_crawled = 0

        existing_pages = self.get_existing_pages()
        print(f"Found {len(existing_pages)} already crawled pages")

        to_visit = {self.base_url}
        self.visited_urls = existing_pages.copy()

        print("Checking existing pages for new links...")
        for url in existing_pages:
            try:
                new_links = await self.get_all_links(url)
                to_visit.update(new_links - self.visited_urls)
            except Exception as e:
                print(f"Error getting links from {url}: {e}")

        print(f"Found {len(to_visit)} new pages to check")

        while to_visit and not self.should_stop:
            current_batch = set()
            while len(current_batch) < batch_size and to_visit:
                url = to_visit.pop()
                if url not in self.visited_urls:
                    current_batch.add(url)
                    self.visited_urls.add(url)
            if not current_batch:
                break
            print(f"Crawling batch of {len(current_batch)} pages...")
            try:
                crawl_tasks = [self.crawl_page(url) for url in current_batch]
                batch_results = await asyncio.gather(*crawl_tasks, return_exceptions=True)
                for result in batch_results:
                    if isinstance(result, str):
                        crawled_files.append(result)
                        pages_crawled += 1
                for url in current_batch:
                    try:
                        new_links = await self.get_all_links(url)
                        to_visit.update(new_links - self.visited_urls)
                    except Exception as e:
                        print(f"Error getting links from {url}: {e}")
            except Exception as e:
                print(f"Error in batch: {e}")
        final_existing_pages = self.get_existing_pages()
        print(f"Crawl complete. New pages added in this run: {pages_crawled}")
        print(f"Total pages in folder: {len(final_existing_pages)}")
        return crawled_files


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: python scraper.py <URL> [output_dir]")
        sys.exit(1)
    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else "crawled_data"
    crawler = WebCrawler(url, output_dir)
    asyncio.run(crawler.crawl_site()) 