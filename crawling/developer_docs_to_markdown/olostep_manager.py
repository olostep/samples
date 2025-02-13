from concurrent.futures import ThreadPoolExecutor, as_completed
import requests
import time
import json
from typing import Dict, List, Optional

# Configuration
API_URL = 'https://api.olostep.com/v1'
API_KEY = '<your_olostep_api_key>'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {API_KEY}'
}

class OlostepManager:
    def __init__(self):
        pass

    def start_crawl(self, start_url: str, max_pages: int = 250, include_urls: Optional[List[str]] = None) -> str:
        """Start a new crawl and return the crawl ID"""
        data = {
            "start_url": start_url,
            "max_pages": max_pages,
            "include_urls": include_urls or [f"{start_url}/**"]
        }
        response = requests.post(f'{API_URL}/crawls', headers=HEADERS, json=data)
        return response.json()['id']

    def await_crawl_completion(self, crawl_id: str):
        """Wait for the crawl to complete"""
        while True:
            response = requests.get(f'{API_URL}/crawls/{crawl_id}', headers=HEADERS)
            pages_count = response.json()['pages_count']
            print(f'Pages completed: {pages_count}')
            if response.json()['status'] == 'completed':
                break
            
            print("Still crawling... Waiting 5 seconds")
            time.sleep(5)

    def get_pages(self, crawl_id: str, formats, max_workers: int = 20) -> List[Dict]:
        """Get all crawled pages with the specified formats content"""
        # Get pages from crawl
        response = requests.get(f'{API_URL}/crawls/{crawl_id}/pages', headers=HEADERS)
        pages = response.json()['pages']
        
        results = []
        total_pages = len(pages)
        
        # Process pages in parallel
        with ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Create futures for content retrieval
            future_to_page = {
                executor.submit(self._retrieve_content, page['retrieve_id'], formats): page
                for page in pages
            }
            
            # Process results as they complete
            for i, future in enumerate(as_completed(future_to_page), 1):
                page = future_to_page[future]
                url = page['url']
                print(f"Processing {i}/{total_pages}: {url}")
                
                try:
                    content_data = future.result()
                    if content_data and "markdown_content" in content_data:
                        results.append({
                            'url': url,
                            'markdown_content': content_data['markdown_content']
                        })
                        print(f"✓ Content retrieved for {url}")
                    else:
                        print(f"⚠ No markdown content for {url}")
                except Exception as e:
                    print(f"❌ Error retrieving content for {url}: {str(e)}")
        
        return results

    def _retrieve_content(self, retrieve_id: str, formats) -> Dict:
        """Retrieves content for a single page."""
        params = {
            "retrieve_id": retrieve_id,
            "formats": json.dumps(formats)
        }
        response = requests.get(f"{API_URL}/retrieve", headers=HEADERS, params=params)
        return response.json()