"""This module is designed for representation Vector class using dunder methods."""

from __future__ import annotations
from math import sqrt


class Vector:
    """Class that represents Vector class."""

    def __init__(self, x_component: int, y_component: int) -> None:
        """Initializes Vector class with x and y coordinates."""
        self.x_component, self.y_component = x_component, y_component

    def get_vector_length(self) -> int | float:
        """Calculates length of Vector and returns it."""
        return sqrt(self.x_component ** 2 + self.y_component ** 2)

    def __add__(self, other: Vector) -> Vector:
        """Adds two Vector together and returns new Vector object."""
        return Vector(self.x_component + other.x_component, self.y_component + other.y_component)

    def __sub__(self, other: Vector) -> Vector:
        """Subtracts two Vector together and returns new Vector object."""
        return Vector(self.x_component - other.x_component, self.y_component - other.y_component)

    def __mul__(self, number: int) -> Vector:
        """Multiplies Vector by number and returns new Vector object."""
        return Vector(self.x_component * number, self.y_component * number)

    def __lt__(self, other: Vector) -> bool:
        """Checks if the length of Vector is less than the other."""
        return self.get_vector_length() < other.get_vector_length()

    def __eq__(self, other: object) -> bool:
        """Checks if the lengths of two Vectors are equal."""
        if not isinstance(other, Vector):
            return NotImplemented
        return self.get_vector_length() == other.get_vector_length()

    def __repr__(self) -> str:
        """Represents numerical Vector as a string in the form of (x,y)."""
        return f"({self.x_component}, {self.y_component})"


if __name__ == "__main__":
    vector_1 = Vector(1, 2)
    vector_2 = Vector(5, 3)
    vector_3 = Vector(1, 2)

    print(f"Sum of {vector_1} and {vector_2} is {vector_1 + vector_2}\n"
          f"Difference of {vector_1} and {vector_2} is {vector_1 - vector_2}\n"
          f"Product of {vector_1} by 2 is {vector_1 * 2}\n"
          f"Is the length of {vector_1} less than the length of {vector_2}? {vector_1 < vector_2}\n"
          f"The length of {vector_1} is {vector_1.get_vector_length()}\n"
          f"The length of {vector_2} is {vector_2.get_vector_length()}\n"
          f"Are the length of{vector_1} and length of {vector_2} equal? {vector_1 == vector_2}\n"
          f"Are the length of {vector_1} and length of {vector_3} equal? {vector_1 == vector_3}")
