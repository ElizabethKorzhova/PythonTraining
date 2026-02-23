"""This script provides iterator for reading the file in reverse order."""
from __future__ import annotations


class ReverseFileIterator:
    """Iterator for reversing the lines in the file."""

    def __init__(self, filename: str) -> None:
        """Initialize the iterator with protected filename."""
        self._filename = filename

    def __iter__(self) -> ReverseFileIterator:
        """Read all lines, initialize new protected attributes and return the iterator object."""
        with open(self._filename, "r", encoding="utf-8") as file:
            self._lines: list[str] = file.readlines()[::-1]
            self._current_index = 0
        return self

    def __next__(self) -> str:
        """Return the next line of the file in the iterator object."""
        if self._current_index == len(self._lines):
            raise StopIteration

        next_line = self._lines[self._current_index]
        self._current_index += 1
        return next_line.strip()


if __name__ == '__main__':
    iterator = ReverseFileIterator("test.txt")
    try:
        for line in iterator:
            print(line)
    except StopIteration:
        pass
