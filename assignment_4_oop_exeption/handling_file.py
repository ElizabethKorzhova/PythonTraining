"""This module is designed for reading numbers from the given text file
and calculating their mean."""

import os


def get_mean_from_file(file_path: str) -> tuple:
    """Gets list of numbers and their arithmetic mean from the given text file."""
    try:
        if os.path.exists(file_path) and os.path.getsize(file_path) == 0:
            raise ValueError("Error: File is empty")
        with open(file_path, "r", encoding="utf-8") as file:
            numbers = []
            for line in file:
                parts = line.split()
                for part in parts:
                    numbers.append(float(part))

            if not numbers:
                raise ValueError("Error: There are not numbers in file")

            average = sum(numbers) / len(numbers)
            return numbers, average
    except FileNotFoundError:
        return None, "Error: File not found"
    except ValueError as ex:
        if "could not convert string to float" in str(ex):
            return None, "Error: File contains non-numeric characters"
        return None, str(ex)


if __name__ == "__main__":
    file_name = "test.txt"
    nums, result = get_mean_from_file(file_name)

    if nums:
        print(f"Numbers from {file_name}: {nums}\nAverage: {result:.2f}")
    else:
        print(result)
