"""This script simulates downloading multiple pages
 asynchronously at the same time."""
from typing import List
import sys
import random

import asyncio


async def download_page(url: str) -> None:
    """Simulate page downloading with random delay."""
    delay = random.randint(1, 5)
    await asyncio.sleep(delay)
    sys.stdout.write(f"Downloaded {url} in {delay} seconds")


async def main(urls: List[str]) -> None:
    """Loads multiple pages asynchronously at the same time."""
    tasks = [download_page(url) for url in urls]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    urls_list = [
        "https://example.com",
        "https://google.com",
        "https://github.com",
    ]

    asyncio.run(main(urls_list))
