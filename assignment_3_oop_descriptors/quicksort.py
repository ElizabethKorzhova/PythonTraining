"""This module is designed to realize Quicksort algorithm and test it on
instances of Person class."""

from __future__ import annotations
from typing import Callable, Any
from person import Person


def fast_sort(list_to_sort: list[Person], key: Callable[[Person], Any]) -> list[Person]:
    """Sorts list in ascending order using Quicksort algorithm."""
    if len(list_to_sort) < 2:
        return list_to_sort

    pivot = list_to_sort[0]
    less = [item for item in list_to_sort[1:] if key(item) <= key(pivot)]
    greater = [item for item in list_to_sort[1:] if key(item) > key(pivot)]

    return fast_sort(less, key) + [pivot] + fast_sort(greater, key)


if __name__ == "__main__":
    persons_list = [
        Person("John", 28),
        Person("Andrew", 28),
        Person("Nick", 20),
    ]

    sorted_list = fast_sort(persons_list, lambda person: (person.age, person.name))
    print("Sorted by age:")
    for person_data in sorted_list:
        print(f"{person_data.name}, {person_data.age} years old")
