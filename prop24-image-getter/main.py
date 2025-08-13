import httpx
import asyncio
import re
import os
import argparse


async def download_image(url):
    try:
        async with httpx.AsyncClient() as client:
            r = await client.get(url)
            r.raise_for_status()

            # Extract filename from URL
            filename = url.split("/")[-2]

            # If no filename or extension, create one
            if not filename or "." not in filename:
                filename = f"image_{filename}.jpg"

            # Create images directory if it doesn't exist
            os.makedirs("images", exist_ok=True)

            # Save image to file
            filepath = os.path.join("images", filename)
            with open(filepath, "wb") as f:
                f.write(r.content)

            print(f"Downloaded: {filename}")
            return filename

    except Exception as e:
        print(f"Error downloading {url}: {e}")
        return None


async def main():
    # Parse command line arguments
    parser = argparse.ArgumentParser(description="Download Property24 listing images")
    parser.add_argument("url", help="Property24 listing URL to scrape images from")
    parser.add_argument(
        "--output",
        "-o",
        default="images",
        help="Output directory for images (default: images)",
    )

    args = parser.parse_args()
    base_url = args.url

    print(f"Scraping images from: {base_url}")

    r = httpx.get(base_url)
    html = r.text

    # Regex pattern to find Property24 image links and remove Ensure1280x720 suffix
    pattern = r'https://images\.prop24\.com/[^"\s]*?Ensure1280x720'

    # Find all image links
    image_links = re.findall(pattern, html)

    # Remove the Ensure1280x720 suffix from each link
    cleaned_links = set([link.replace("Ensure1280x720", "") for link in image_links])

    print(f"Found {len(cleaned_links)} unique image links")

    # Create download tasks
    tasks = [download_image(url) for url in cleaned_links]

    # Download all images concurrently
    results = await asyncio.gather(*tasks, return_exceptions=True)

    # Count successful downloads
    successful = [r for r in results if r is not None]
    print(
        f"Successfully downloaded {len(successful)} images to '{args.output}/' directory"
    )


if __name__ == "__main__":
    asyncio.run(main())
