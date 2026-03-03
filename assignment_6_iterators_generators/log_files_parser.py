"""This script provides generator that reads the file line by line and returns only
lines with errors (status code 4XX or 5XX). Also provides storing these errors to
the separate file for further analysis."""
import re
from typing import Generator


def find_errors(log_file: str) -> Generator:
    """Reads the given log file and yields lines with errors."""
    with open(log_file, "r", encoding="utf-8") as file:
        for line in file:
            search_result = re.search(r" [45]\d{2} ", line)
            if search_result:
                yield line


if __name__ == '__main__':
    generator = find_errors("test.log")

    with open("errors.log", "w+", encoding="utf-8") as errors_file:
        for error in generator:
            errors_file.write(error)
