"""Downloading image from the network."""
import sys
import threading
from pathlib import Path
import requests

URLS = [
    "https://plus.unsplash.com/premium_photo-1666900440561-94dcb6865554?q=80&w=1527&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1493612276216-ee3925520721?q=80&w=1528&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://images.unsplash.com/photo-1507608616759-54f48f0af0ee?q=80&w=1587&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
    "https://plus.unsplash.com/premium_photo-1666901328734-3c6eb9b6b979?q=80&w=1760&auto=format&fit=crop&ixlib=rb-4.1.0&ixid=M3wxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8fA%3D%3D",
]

OUTPUT_DIR = Path("downloads")
OUTPUT_DIR.mkdir(exist_ok=True)

lock = threading.Lock()

def download_image(image_url: str, image_index: int) -> None:
    """Downloads image from the network."""
    filename = f"image_{image_index}.jpg"
    output_path = OUTPUT_DIR / filename

    with lock:
        sys.stdout.write(f"Downloading {output_path}...\n")

    response = requests.get(image_url)

    with open(output_path, "wb") as file:
        file.write(response.content)

    sys.stdout.write(f"Done: {output_path}\n")


if __name__ == "__main__":
    threads = []

    for index, url in enumerate(URLS, start=1):
        thread = threading.Thread(target=download_image, args=(url, index))
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()