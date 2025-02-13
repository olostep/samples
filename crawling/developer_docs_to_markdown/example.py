from olostep_manager import OlostepManager
import time
from datetime import datetime

def main():
    # Initialize the Olostep manager
    olostep = OlostepManager()
    
    # Record start time for crawl duration tracking
    crawl_start_time = time.time()
    
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Starting documentation crawl...")
    
    # Start crawl with parameters and wait to complete
    crawl_id = olostep.start_crawl(
        start_url="https://docs.stripe.com/payments/checkout/",
        max_pages=100,
        include_urls=["/payments/checkout/**"] #only include /payment/checkout/ pages
    )
    
    # Wait for the crawl to complete
    olostep.await_crawl_completion(crawl_id)
    
    # Calculate and display crawl duration
    crawl_duration = time.time() - crawl_start_time
    print(f"[{datetime.now().strftime('%H:%M:%S')}] Crawl completed in {crawl_duration:.2f} seconds")

    # Fetch crawled documentation pages with their markdown content
    pages = olostep.get_pages(crawl_id=crawl_id, formats=["markdown"])
    print(f"Found {len(pages)} pages to process")

    # Save all markdown content to a single file
    output_file = "doc_markdown.md"
    
    with open(output_file, "w", encoding="utf-8") as f:
        for page in pages:
            url = page['url']
            content = page['markdown_content']
            
            # Write page header and content
            f.write(f"## URL: {url}\n\n")  # Add URL as a heading
            f.write(f"{content}\n\n")       # Add page content
            f.write("---\n\n")              # Add separator between pages
            
            print(f"✓ Added content from {url}")

    print(f"\n✅ Process complete! All content has been saved to '{output_file}'")
    print(f"Total pages processed: {len(pages)}")


if __name__ == "__main__":
    main()