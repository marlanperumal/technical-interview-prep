import asyncio
import httpx
import re
from urllib.parse import urljoin, urldefrag

# Regex for extracting hrefs (very basic)
HREF_RE = re.compile(r'href=[\'"]?([^\'" >]+)', re.IGNORECASE)


async def fetch(client, url):
    """Fetch page content for a given URL."""
    try:
        resp = await client.get(url, timeout=5.0)
        if resp.status_code == 200 and "text/html" in resp.headers.get(
            "content-type", ""
        ):
            return resp.text
    except httpx.RequestError:
        pass
    return None


def extract_links(base_url, html):
    """Extract absolute URLs from HTML text."""
    links = set()
    for match in HREF_RE.findall(html):
        # Remove any fragment (part after #)
        clean_url = urldefrag(urljoin(base_url, match))[0]
        if clean_url.startswith("http"):
            links.add(clean_url)
    return links


async def crawl(start_url, max_depth):
    visited = set()
    to_visit = {start_url}
    async with httpx.AsyncClient(follow_redirects=True) as client:
        for depth in range(max_depth):
            print(f"Depth {depth}: {len(to_visit)} URLs to visit")
            tasks = [fetch(client, url) for url in to_visit if url not in visited]
            pages = await asyncio.gather(*tasks)

            new_links = set()
            for url, html in zip(to_visit, pages):
                visited.add(url)
                if html:
                    new_links.update(extract_links(url, html))

            to_visit = new_links - visited

    return visited


if __name__ == "__main__":
    urls = asyncio.run(crawl("https://stuntedchicken.co.za", 3))
    print(f"Crawled {len(urls)} pages")
    for u in urls:
        print(u)
