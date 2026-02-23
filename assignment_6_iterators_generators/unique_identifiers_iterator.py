"""This script provides iterator that generate unique identifiers."""
import uuid


class UniqueIdentifiersIterator:
    """Iterator for generating unique identifiers."""

    def __iter__(self) -> UniqueIdentifiersIterator:
        """Return the iterator object."""
        return self

    def __next__(self) -> object:
        """Generate the next unique identifier and return it.."""
        return uuid.uuid4()


if __name__ == "__main__":
    iterator = UniqueIdentifiersIterator()
    for _ in range(10):
        print(next(iterator))
