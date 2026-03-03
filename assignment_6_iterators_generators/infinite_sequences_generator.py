"""This script provides generator that generates an infinite sequence of even numbers."""
from typing import Generator


def generate_infinite_sequences(limit: int | None = None) -> Generator:
    """Function that generates infinite sequences."""
    count = 0
    while True:
        yield count
        count += 2
        if limit is not None and count > limit:
            break


if __name__ == '__main__':
    with open("infinite_sequences.txt", "w+", encoding="utf-8") as file:
        generator = generate_infinite_sequences(100)
        for sequence in generator:
            file.write(str(sequence) + "\n")
