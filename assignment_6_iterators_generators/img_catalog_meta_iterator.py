"""This script is designed to implement ImgMetaIterator which opens each image in turn,
extracts metadata from it and saves this data to a CSV file."""
from __future__ import annotations

import csv
import os

from PIL import Image, ExifTags

IMG_DIR_PATH = os.getcwd() + "/test_img"
META_DIR = "./metas/"


class ImgMetaIterator:
    """Iterator for extracting metadata from image and saving data to the CSV file."""

    def __init__(self, folder_path: str) -> None:
        """Initialize the iterator with protected folder_path."""
        self._folder_path = folder_path

    def __iter__(self) -> ImgMetaIterator:
        """Gets all images in directory, initialize new protected attributes
        and return the iterator object."""
        self._img_list = os.listdir(self._folder_path)
        self._current_index = 0
        return self

    def __next__(self):
        """Return the next image in the iterator object."""
        if self._current_index >= len(self._img_list):
            raise StopIteration
        current_meta = self._get_meta()
        self._store_meta_to_csv(current_meta)
        next_photo = self._img_list[self._current_index]
        self._current_index += 1
        return next_photo

    def _get_meta(self) -> list[list[str]]:
        """Finds metadata from image and returns it as the list."""
        img_path = "./test_img/" + self._img_list[self._current_index]
        with Image.open(img_path) as img:
            exif_data = img.getexif()
        metadata: list[list[str]] = []
        for tag_id in exif_data:
            tag = ExifTags.TAGS.get(tag_id, tag_id)
            data = exif_data.get(tag_id)
            if isinstance(data, bytes):
                data = data.decode()
            metadata.append([tag, data])
        return metadata

    def _store_meta_to_csv(self, metadata: list[list[str]]) -> None:
        """Writes metadata from image to CSV file."""
        file_path = (META_DIR +
                     os.path.splitext(self._img_list[self._current_index])[0]
                     + ".csv")
        if not os.path.exists(META_DIR):
            os.makedirs(META_DIR)

        with open(file_path, "w+", encoding="utf-8") as csv_file:
            writer = csv.writer(csv_file)
            if metadata:
                writer.writerows(metadata)
            else:
                writer.writerow(["No metadata available"])


if __name__ == '__main__':
    try:
        img_data = ImgMetaIterator(IMG_DIR_PATH)
        for photo in img_data:
            print(photo)
    except FileNotFoundError as exception:
        print(exception)
