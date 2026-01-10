"""This module is designed to represent Person class using dunder methods and implement
sorting objects by age."""

from __future__ import annotations


class Person:
    """Class that represents Person."""

    def __init__(self, name: str, age: int) -> None:
        """Initializes Person class with name and age."""
        self.__name, self.__age = name, age

    @property
    def name(self) -> str:
        """Gets name of person."""
        return self.__name

    @property
    def age(self) -> int:
        """Gets age of person."""
        return self.__age

    def __lt__(self, other: Person) -> bool:
        """Checks if the Person is younger than the other."""
        return self.age < other.age

    def __gt__(self, other: Person) -> bool:
        """Checks if the Person is older than the other."""
        return self.age > other.age

    def __eq__(self, other: object) -> bool:
        """Checks if two Person are the same age."""
        if not isinstance(other, Person):
            return NotImplemented
        return self.age == other.age


if __name__ == "__main__":
    person_list = [
        Person("Jack", 28),
        Person("Nick", 18),
        Person("Anna", 34),
        Person("Bob", 30),
        Person("Marry", 30)
    ]

    person_list.sort(key=lambda person: person.age)

    print("Sorted by age:")
    for person_data in person_list:
        print(f"{person_data.name}, {person_data.age} years old")

    print(f"\nIs {person_list[0].name} older than {person_list[3].name}?\n"
          f" {person_list[0] > person_list[3]}\nIs {person_list[1].name} younger then "
          f"{person_list[2].name}?\n {person_list[1] < person_list[2]}\nAre {person_list[3].name} "
          f"and {person_list[4].name}the same age?\n {person_list[3] == person_list[4]}")
