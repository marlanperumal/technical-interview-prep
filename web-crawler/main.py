import re
import httpx


def crawl(base_url: str, max_depth: int = 2) -> list[str]:
    """
    Crawl the given start URL and return a list of all the URLs found on the page,
    and recursively all the URLs found on those pages up to a depth of `max_depth`
    """

    links: set[str] = set()

    def crawl_link(client: httpx.Client, link: str, depth: int = 0):
        if depth == max_depth:
            return

        r = client.get(link)

        html = r.text

        pattern = r'<a[^>]+href=["\']([^"\']+)["\'][^>]*>'
        new_links = set(re.findall(pattern, html, re.IGNORECASE))
        deduped_new_links = new_links.difference(links)
        links.update(new_links)

        for link in deduped_new_links:
            print(depth, link)
            crawl_link(client, link, depth + 1)

    with httpx.Client(base_url=base_url) as client:
        crawl_link(client, base_url)

    return links


if __name__ == "__main__":
    links = crawl("https://stuntedchicken.co.za", 2)
