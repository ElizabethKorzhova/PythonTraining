"""This script provides FileCatalogIterator that iterates over all files in given directory
and return in one by one with their name and size."""
from __future__ import annotations
import os

DIR_NAME = "metas"
DIR_PATH = os.getcwd() + "/" + DIR_NAME


class FilesCatalogIterator:
    """Iterator to return all files in the specified directory one by one and its name and size."""

    def __init__(self, folder_path: str) -> None:
        """Initialize the iterator with protected folder_path."""
        self._folder_path = folder_path

    def __iter__(self) -> FilesCatalogIterator:
        """Gets all images in directory, initialize new protected attributes
        and return the iterator object."""
        self._total_files = os.listdir(self._folder_path)
        self._current_index = 0
        return self

    def __next__(self) -> str:
        """Return the next image data (name, extension and size in bytes) in the iterator object."""
        if self._current_index >= len(self._total_files):
            raise StopIteration
        file_data = os.path.splitext(self._total_files[self._current_index])
        size = os.path.getsize(self._folder_path)
        self._current_index += 1
        return (f"File name: {file_data[0]}\n\tfile extension: "
                f"{file_data[1][1:]}\n\tfile size: {size} bytes\n")


if __name__ == '__main__':
    iterator = FilesCatalogIterator(DIR_PATH)
    for file in iterator:
        print(file)
