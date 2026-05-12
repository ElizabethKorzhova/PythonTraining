"""Asynchronous loading images from multiple websites."""
from pathlib import Path

import asyncio
import aiohttp


async def download_image(url: str, filename: str) -> None:
    """Download image asynchronously and save it."""
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(url) as response:
                response.raise_for_status()
                content = await response.read()

        Path(filename).write_bytes(content)
        print(f"Saved image: {filename}")

    except aiohttp.ClientError as error:
        print(f"Failed to download {url}: {error}")


async def main() -> None:
    """Orchestrates the concurrent downloading of multiple images."""
    images = [
        (
            "https://plus.unsplash.com/premium_photo-1666900440561-94dcb6865554?q=80&w=1527&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_1.jpg",
        ),
        (
            "https://images.unsplash.com/photo-1493612276216-ee3925520721?q=80&w=1528&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_2.jpg",
        ),
        (
            "https://images.unsplash.com/photo-1507608616759-54f48f0af0ee?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
            "image_3.jpg",
        ),
    ]

    tasks = [download_image(url, filename) for url, filename in images]
    await asyncio.gather(*tasks)


if __name__ == "__main__":
    asyncio.run(main())