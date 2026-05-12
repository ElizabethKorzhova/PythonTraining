"""Fetch content from websites asynchronously."""
from typing import List

import asyncio
import aiohttp


async def fetch_content(url: str) -> str:
    """Fetch page content asynchronously."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                return await response.text()

    except aiohttp.ClientError as error:
        return f"Request error for {url}: {error}"


async def fetch_all(urls: List[str]) -> List[str]:
    """Fetch all pages asynchronously."""
    tasks = [fetch_content(url) for url in urls]
    return await asyncio.gather(*tasks)


async def main() -> None:
    """Gets results and prints them."""
    urls = [
        "https://example.com",
        "https://httpbin.org/get",
        "https://github.com",
    ]

    results = await fetch_all(urls)

    for url, content in zip(urls, results):
        print(f"\nURL: {url}")
        print(content[:200])


if __name__ == "__main__":
    asyncio.run(main())
