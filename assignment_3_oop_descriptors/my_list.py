"""This module is designed for implementing custom versions of the len(), sum(),
and min() build-in functions."""

from typing import Iterator


class MyList:
    """Class that represents list of numbers."""

    def __init__(self, my_list: list[int | float]) -> None:
        """Initializes MyList class."""
        self.__my_list = my_list

    @property
    def my_list(self) -> list[int | float]:
        """Getter for my_list."""
        return self.__my_list

    def __len__(self) -> int:
        """Gets the length of the MyList."""
        count = 0
        for _ in self.my_list:
            count += 1
        return count

    def __iter__(self) -> Iterator[int | float]:
        """Converts MyList into the iterator."""
        return iter(self.my_list)

    def __getitem__(self, index: int) -> int | float:
        """Gets item from MyList at the given index."""
        return self.my_list[index]


def my_sum(my_list: MyList) -> int | float:
    """Calculates sum of items in the list."""
    total: int | float = 0
    for item in my_list:
        total += item
    return total


def my_min(my_list: MyList) -> int | float:
    """Find minimum item in the list."""
    if len(my_list) == 0:
        raise ValueError("Cannot find minimum item in empty list")

    min_number: int | float = my_list[0]
    for item in my_list:
        if item < min_number:
            min_number = item
    return min_number


numbers_list = MyList([2, 1.5, 3, 0.5])
empty_list = MyList([])
print(f"List: {numbers_list.my_list}\nLength of the list: {len(numbers_list)}"
      f"\nSum result: {my_sum(numbers_list)}\nMinimum number in the list: {my_min(numbers_list)}\n"
      f"\nEmpty list result check: {empty_list.my_list}\n"
      f"Length of the list: {len(empty_list)}\nSum result: {my_sum(empty_list)}\n")
print(my_min(empty_list))
