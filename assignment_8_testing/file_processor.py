"""Module provides FileProcessor class"""
import os


class FileProcessor:
    """Class represents FileProcessor class"""

    @staticmethod
    def write_to_file(file_path: str, data: str) -> None:
        """
        Writes given data to the file
        :param file_path: path to file (string)
        :param data: data to write to file (string)
        """
        with open(file_path, "w", encoding="utf-8") as file:
            file.write(data)

    @staticmethod
    def read_from_file(file_path: str) -> str:
        """
        Reads data from the given file
        :param file_path: path to file (string)
        """
        if not os.path.exists(os.path.dirname(file_path)):
            raise FileNotFoundError(f"File {file_path} path does not exist")
        with open(file_path, "r", encoding="utf-8") as file:
            data = file.read()
            return data
