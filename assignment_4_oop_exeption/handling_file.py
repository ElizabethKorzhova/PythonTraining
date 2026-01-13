"""This module is designed for reading numbers from the given text file
and calculating their mean."""

import re
import os


def get_numbers_from_file(file_path: str) -> list[int]:
    """Gets list of numbers from the given text file."""
    if os.path.getsize(file_path) == 0:
        raise ValueError("File is empty")

    with open(file_path, "r", encoding="utf-8") as file:
        data = file.read()

    if not bool(re.fullmatch(r"^[\d\s]+$", data)) or bool(re.fullmatch(
            r"^\s+$", data)):
        raise ValueError("File contains non-numeric characters or non-integer numbers")

    numbers = list(map(int, re.findall(r"\d+", data)))
    return numbers


def mean(numbers: list[int]) -> int | float:
    """Calculates the mean of a list of numbers."""
    if len(numbers) == 1:
        return numbers[0]

    return sum(numbers) / len(numbers)


if __name__ == "__main__":
    try:
        numbers_list = get_numbers_from_file("test.txt")
        print(f"List of numbers from the given file: {numbers_list}\n"
              f"Mean: {mean(numbers_list)}")

    except (FileNotFoundError, ValueError) as ex:
        print(ex)
