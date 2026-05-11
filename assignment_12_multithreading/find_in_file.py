"""Search text in multiple files concurrently using threads."""
import sys
import threading
from pathlib import Path

FILES = [
    Path("file1.txt"),
    Path("file2.txt"),
    Path("file3.txt"),
]

SEARCH_TEXT = "Test"


def search_in_file(file_path: Path, text: str) -> None:
    """Search text in file."""
    try:
        with file_path.open("r", encoding="utf-8") as file:
            for line_number, line in enumerate(file, start=1):
                if text in line:
                    sys.stdout.write(f"{file_path}: line {line_number}: {line.strip()}\n")

    except FileNotFoundError:
        sys.stdout.write(f"File not found: {file_path}\n")


if __name__ == "__main__":
    threads = []

    for path in FILES:
        thread = threading.Thread(target=search_in_file, args=(path, SEARCH_TEXT),)
        thread.start()
        threads.append(thread)

    for thread in threads:
        thread.join()

    sys.stdout.write("Search finished.")