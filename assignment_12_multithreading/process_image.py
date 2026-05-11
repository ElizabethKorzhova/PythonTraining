"""Resize images concurrently."""
import sys
from concurrent.futures import ProcessPoolExecutor
from pathlib import Path

from PIL import Image

INPUT_DIR = Path("downloads")
OUTPUT_DIR = Path("resized")
OUTPUT_DIR.mkdir(exist_ok=True)
SIZE = (200, 200)


def process_image(image_path: Path) -> None:
    """Resizes an image."""
    with Image.open(image_path) as image:
        image.thumbnail(SIZE)
        output_path = OUTPUT_DIR / image_path.name
        image.save(output_path)

    sys.stdout.write(f"Processed: {image_path.name}\n")


if __name__ == "__main__":
    images = list(INPUT_DIR.glob("*.jpg"))

    with ProcessPoolExecutor() as executor:
        results = executor.map(process_image, images)
