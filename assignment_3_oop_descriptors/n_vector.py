"""This module is designed for representation NVector n-dimensional space
class using dunder methods."""

from __future__ import annotations
from math import sqrt


class NVector:
    """Class that represents a vector in n-dimensional space."""

    def __init__(self, coordinates: list[int]) -> None:
        """Initializes NVector with coordinates."""
        self.__coordinates = coordinates

    @property
    def coordinates(self) -> list[int]:
        """Gets the coordinates of the vector."""
        return self.__coordinates

    def __repr__(self):
        """Represents NVector as a string in the form of (x1, x2, ..., xn)."""
        return f"({', '.join(str(coordinate) for coordinate in self.__coordinates)})"

    def __add__(self, other: NVector) -> NVector:
        """Adds two vectors."""
        self.check_dimension(other)
        return NVector(
            [coord_self + coord_other
             for coord_self, coord_other in zip(self.__coordinates, other.coordinates)]
        )

    def __sub__(self, other: NVector) -> NVector:
        """Subtracts two vectors."""
        self.check_dimension(other)
        return NVector(
            [coord_self - coord_other
             for coord_self, coord_other in zip(self.__coordinates, other.coordinates)]
        )

    def __mul__(self, other: NVector) -> int:
        """Calculates dot product of two n-dimensional vectors."""
        self.check_dimension(other)
        return sum(
            coord_self * coord_other
            for coord_self, coord_other in zip(self.__coordinates, other.coordinates)
        )

    def __lt__(self, other: NVector) -> bool:
        """Checks if the length of NVector is less than the other."""
        return self.magnitude() < other.magnitude()

    def __gt__(self, other: NVector) -> bool:
        """Checks if the length of NVector is greater than the other."""
        return self.magnitude() > other.magnitude()

    def __eq__(self, other: object) -> bool:
        """Checks if the lengths of two NVectors are equal."""
        if not isinstance(other, NVector):
            return NotImplemented
        return self.magnitude() == other.magnitude()

    def check_dimension(self, other: NVector) -> None:
        """Checks if two vectors have the different dimension."""
        if len(self.__coordinates) != len(other.coordinates):
            raise ValueError("Cannot perform operation on vectors that have different dimensions.")

    def magnitude(self) -> int | float:
        """Calculates the magnitude (length) of the vector."""
        return sqrt(sum(coord ** 2 for coord in self.__coordinates))


vector_1 = NVector([1, 2, 3, 5, 9])
vector_2 = NVector([4, 5, 6, 10, 12])
print(f"Sum of {vector_1} and {vector_2} is {vector_1 + vector_2}\n"
      f"Difference of {vector_1} and {vector_2} is {vector_1 - vector_2}\n"
      f"Dot product of {vector_1} and {vector_2} is {vector_1 * vector_2}\n"
      f"The length of {vector_1} is {vector_1.magnitude()}\n"
      f"The length of {vector_2} is {vector_2.magnitude()}\n"
      f"Is the length of {vector_1} less than the length of {vector_2}? {vector_1 < vector_2}\n"
      f"Is the length of {vector_1} greater than the length of {vector_2}? {vector_1 > vector_2}\n"
      f"Are the length of{vector_1} and length of {vector_2} equal? {vector_1 == vector_2}\n")
