"""This script compare multithreading, multiprocessing, and asynchronous"""
import asyncio
import time
from collections.abc import Callable
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor

import aiohttp
import requests

URL = "https://example.com"
REQUESTS_COUNT = 500


def sync_request(url: str) -> int:
    """Sends synchronous HTTP request."""
    response = requests.get(url, timeout=10)
    return response.status_code


def run_sync() -> None:
    """Executes requests synchronously."""
    for _ in range(REQUESTS_COUNT):
        sync_request(URL)


def run_threads() -> None:
    """Executes requests using multithreading."""
    with ThreadPoolExecutor(max_workers=50) as executor:
        list(executor.map(sync_request, [URL] * REQUESTS_COUNT))


def run_processes() -> None:
    """Execute requests using multiprocessing."""
    with ProcessPoolExecutor(max_workers=8) as executor:
        list(executor.map(sync_request, [URL] * REQUESTS_COUNT))


async def async_request(session: aiohttp.ClientSession, url: str) -> int | None:
    """Send asynchronous HTTP request."""
    try:
        async with session.get(url) as response:
            return response.status

    except aiohttp.ClientError as error:
        print(f"Async request error: {error}")
        return None


async def run_async() -> None:
    """Execute requests asynchronously."""
    async with aiohttp.ClientSession() as session:
        tasks = [async_request(session, URL) for _ in range(REQUESTS_COUNT)]
        await asyncio.gather(*tasks)


def measure_time(name: str, func: Callable) -> None:
    """Measure execution time for synchronous function."""
    print(f"\nStarting {name}...")
    start = time.perf_counter()
    func()
    end = time.perf_counter()
    print(f"{name}: {end - start:.2f} seconds")


async def measure_async_time() -> None:
    """Measure execution time for asynchronous requests."""
    print("\nStarting Async...")
    start = time.perf_counter()
    await run_async()
    end = time.perf_counter()
    print(f"Async: {end - start:.2f} seconds")


if __name__ == "__main__":
    measure_time("Sync", run_sync)
    measure_time("Threads", run_threads)
    measure_time("Processes", run_processes)

    asyncio.run(measure_async_time())
    print("\nAll tests completed.")