# Developer Docs To Markdown for LLM Context

Extract documentation from any website into markdown format - perfect for feeding into LLMs to get accurate answers about specific products/APIs.

## Quick Start

1. Get API key from [olostep.com/auth](https://olostep.com/auth)
2. Update `olostep_manager.py`:
```python
API_KEY = '<your_olostep_api_key>'
```
3. Run:
```bash
python example.py
```

Demonstrated on Stripe's Checkout docs:
- Crawled 63 pages in 54.96 seconds
- Converted to clean markdown

## Sample Output

Check [`./output/doc_markdown.md`](./output/doc_markdown.md) for the output.

## Implementation

- [`example.py`](./example.py) - Main crawler
- [`olostep_manager.py`](./olostep_manager.py) - API wrapper