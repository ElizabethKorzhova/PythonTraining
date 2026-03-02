"""This script is designed to implement generator that reads the large text file
line by line, returns only lines that contain the given keyword and write the matching
lines to the new file."""
from typing import Generator

FILE = "test_file.txt"


def process_large_file(file_name: str, keyword: str) -> Generator:
    """Generator that reads large text file and yields lines that contain keyword."""
    with open(file_name, "r", encoding="utf-8") as file:
        for line in file:
            if keyword.lower() in line.lower():
                yield line


def write_data_to_txt(file_path: str, generator: Generator) -> None:
    """Function that writes matching lines to the separate text file."""
    with open(file_path, "w+", encoding="utf-8") as file:
        for line in generator:
            file.write(line)


if __name__ == '__main__':
    try:
        test_generator = process_large_file(FILE, "test")
        write_data_to_txt("filtered_" + FILE, test_generator)
    except FileNotFoundError as exception:
        print(exception)
