import re
import httpx
import asyncio
from urllib.parse import urljoin, urlparse


async def crawl_web(start_url: str, max_depth: int = 2) -> set[str]:
    """
    Crawl the web starting from a URL up to a specified depth.
    Uses concurrent crawling to speed up the process.

    Args:
        start_url: The starting URL to crawl
        max_depth: Maximum depth to crawl (0 = just start URL)

    Returns:
        Set of all discovered URLs
    """
    discovered_urls = set()
    visited_urls = set()

    async def crawl_page(client: httpx.AsyncClient, url: str, depth: int = 0):
        # Skip if already visited or exceeded depth
        if depth > max_depth or url in visited_urls:
            return

        visited_urls.add(url)
        discovered_urls.add(url)

        try:
            # Fetch the page
            response = await client.get(url, timeout=10.0)
            response.raise_for_status()

            # Extract links using regex
            html = response.text
            link_pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>'
            found_links = re.findall(link_pattern, html, re.IGNORECASE)

            # Convert relative URLs to absolute URLs
            absolute_links = set()
            for link in found_links:
                if link.startswith(("http://", "https://")):
                    absolute_links.add(link)
                elif link.startswith("/"):
                    parsed_current = urlparse(
                        url
                    )  # Use current page URL, not start_url
                    absolute_links.add(
                        f"{parsed_current.scheme}://{parsed_current.netloc}{link}"
                    )
                elif not link.startswith(("#", "javascript:", "mailto:")):
                    absolute_links.add(
                        urljoin(url, link)
                    )  # Use current page URL as base

            # Filter out non-HTTP links and already visited
            new_links = absolute_links - visited_urls

            # Create concurrent tasks for next depth
            if depth < max_depth and new_links:
                tasks = [
                    asyncio.create_task(crawl_page(client, link, depth + 1))
                    for link in new_links
                ]
                await asyncio.gather(*tasks, return_exceptions=True)

        except Exception as e:
            print(f"Error crawling {url}: {e}")

    # Start crawling with concurrent client
    async with httpx.AsyncClient(follow_redirects=True) as client:
        await crawl_page(client, start_url)

    return discovered_urls


# Example usage
async def main():
    urls = await crawl_web("https://stuntedchicken.co.za", max_depth=2)
    print(f"Discovered {len(urls)} URLs:")
    for url in sorted(urls):
        print(f"  {url}")


if __name__ == "__main__":
    asyncio.run(main())
