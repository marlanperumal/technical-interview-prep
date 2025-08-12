import re
import httpx
import asyncio


async def crawl(base_url: str, max_depth: int = 2) -> list[str]:
    """
    Crawl the given start URL and return a list of all the URLs found on the page,
    and recursively all the URLs found on those pages up to a depth of `max_depth`
    """

    links: set[str] = set()
    visited: set[str] = set()

    async def crawl_link(client: httpx.Client, link: str, depth: int = 0):
        if depth > max_depth or link in visited:
            return

        visited.add(link)

        print(depth, link)
        r = await client.get(link)

        html = r.text

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>'
        new_links = set(re.findall(pattern, html, re.IGNORECASE))
        deduped_new_links = new_links.difference(links)
        links.update(new_links)

        tasks = [
            asyncio.create_task(crawl_link(client, link, depth + 1))
            for link in deduped_new_links
        ]

        if tasks:
            await asyncio.gather(*tasks)

    async with httpx.AsyncClient(base_url=base_url) as client:
        await crawl_link(client, base_url)

    print(len(links))


if __name__ == "__main__":
    asyncio.run(crawl("https://stuntedchicken.co.za", 2))
