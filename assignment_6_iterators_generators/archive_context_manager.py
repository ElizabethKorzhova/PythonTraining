"""This script is designed to implement custom context manager ArchiveContextManager
that automatically creates the archive, adds files, and after exiting completes the archiving."""
import os
import zipfile
from typing import Optional


class ArchiveContextManager:
    """Context manager to create the archive and to add files to it."""

    def __init__(self, dir_path: str) -> None:
        """Initialize context manager with dir_path parameter to create archive
        and to add files to it.."""
        self._dir_path = dir_path
        self._dir_name = os.path.basename(dir_path)
        self._zip_file: Optional[zipfile.ZipFile] = None

    def __enter__(self) -> zipfile.ZipFile:
        """Creates the archive, adds file to it and returns zipfile object."""
        if not os.path.exists(self._dir_path):
            raise FileNotFoundError("Directory does not exist")

        self._zip_file = zipfile.ZipFile(self._dir_path + ".zip", "w")
        for file in os.listdir(self._dir_path):
            self._zip_file.write(self._dir_name + "/" + file)
        return self._zip_file

    def __exit__(self, exc_type, exc_val, exc_tb):
        """Closes the archive."""
        if self._zip_file:
            self._zip_file.close()


if __name__ == '__main__':
    with ArchiveContextManager("test_img") as zip_file:
        print(zip_file)
