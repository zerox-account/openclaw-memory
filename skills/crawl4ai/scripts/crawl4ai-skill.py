#!/usr/bin/env python3
"""
Crawl4AI Skill for OpenClaw
Web scraping tool for extracting clean content from websites
"""

import asyncio
import sys
import json
import os
from urllib.parse import urlparse

try:
    from crawl4ai import AsyncWebCrawler, BrowserConfig, CrawlerRunConfig
    NEW_API = True
except ImportError:
    from crawl4ai import AsyncWebCrawler
    NEW_API = False

async def scrape_site(url, output_dir=None):
    """Scrape a website and save content as markdown"""
    
    # Create output directory
    if not output_dir:
        domain = urlparse(url).netloc.replace(".", "_")
        output_dir = f"./scraped_{domain}"
    
    os.makedirs(output_dir, exist_ok=True)
    
    print(f"🕷️  Crawl4AI Skill")
    print(f"   Target: {url}")
    print(f"   Output: {output_dir}/")
    print()
    
    try:
        if NEW_API:
            # New Crawl4AI v0.5+ API
            browser_config = BrowserConfig(headless=True, verbose=False)
            run_config = CrawlerRunConfig(
                word_count_threshold=10,
                excluded_tags=['nav', 'footer', 'aside', 'header'],
                remove_overlay_elements=True
            )
            
            async with AsyncWebCrawler(config=browser_config) as crawler:
                result = await crawler.arun(url=url, config=run_config)
                
                markdown_content = result.markdown.fit_markdown if hasattr(result, 'markdown') else str(result)
                title = result.metadata.get('title', 'Untitled') if hasattr(result, 'metadata') else 'Untitled'
                timestamp = str(result.timestamp) if hasattr(result, 'timestamp') else 'unknown'
        else:
            # Legacy API
            async with AsyncWebCrawler(verbose=True) as crawler:
                result = await crawler.arun(url=url)
                markdown_content = result.markdown
                title = result.metadata.get('title', 'Untitled')
                timestamp = result.timestamp
        
        # Save main page
        safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")[:80]
        output_file = f"{output_dir}/{safe_name}.md"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**URL:** {url}\n\n")
            f.write(f"**Scraped:** {timestamp}\n\n")
            f.write("---\n\n")
            f.write(markdown_content)
        
        # Create index
        index = {
            "source_url": url,
            "scraped_at": timestamp,
            "title": title,
            "word_count": len(markdown_content.split()),
            "files": [f"{safe_name}.md"]
        }
        
        with open(f"{output_dir}/_index.json", "w") as f:
            json.dump(index, f, indent=2)
        
        print(f"✅ Scraped successfully!")
        print(f"   Pages: 1")
        print(f"   Words: {index['word_count']}")
        print(f"   Saved: {output_file}")
        
        return output_dir
        
    except Exception as e:
        print(f"❌ Error: {e}")
        print(f"   Trying fallback method...")
        
        # Fallback: simple request
        import requests
        from bs4 import BeautifulSoup
        
        response = requests.get(url, timeout=30)
        soup = BeautifulSoup(response.content, 'html.parser')
        
        title = soup.title.string if soup.title else 'Untitled'
        
        # Remove script and style elements
        for script in soup(["script", "style", "nav", "footer", "header"]):
            script.decompose()
        
        text = soup.get_text(separator='\n', strip=True)
        
        safe_name = url.replace("https://", "").replace("http://", "").replace("/", "_")[:80]
        output_file = f"{output_dir}/{safe_name}.md"
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(f"# {title}\n\n")
            f.write(f"**URL:** {url}\n\n")
            f.write(f"**Scraped:** {asyncio.get_event_loop().time()}\n\n")
            f.write("---\n\n")
            f.write(text)
        
        print(f"✅ Scraped with fallback method!")
        print(f"   Words: {len(text.split())}")
        
        return output_dir

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage: python3 crawl4ai-skill.py <url> [output_dir]")
        print("Example: python3 crawl4ai-skill.py https://example.com ./output")
        sys.exit(1)
    
    url = sys.argv[1]
    output_dir = sys.argv[2] if len(sys.argv) > 2 else None
    
    result = asyncio.run(scrape_site(url, output_dir))
    print(f"\n🎯 Ready for OpenClaw import: {result}/")
