"""This module is designed for representation BinaryNumber class using dunder
methods to operation on it."""

from __future__ import annotations


class BinaryNumber:
    """ Class that represents Binary Number."""

    def __init__(self, bin_number: str) -> None:
        """Initializes BinaryNumber class with bin_number represented
        as a string."""
        if not isinstance(bin_number, str):
            raise TypeError("Binary Number must be represented as s string")

        if any(digit not in "01" for digit in bin_number):
            raise ValueError("Binary Number must be include only 0 or 1")

        self.__bin_number = bin_number

    @property
    def bin_number(self) -> str:
        """Gets binary number."""
        return self.__bin_number

    def __and__(self, other: BinaryNumber) -> str:
        """Does bitwise AND between two binary numbers."""
        return bin(int(self.bin_number, 2) & int(other.bin_number, 2))[2:]

    def __or__(self, other: BinaryNumber) -> str:
        """Does bitwise OR between two binary numbers."""
        return bin(int(self.bin_number, 2) | int(other.bin_number, 2))[2:]

    def __xor__(self, other: BinaryNumber) -> str:
        """Does bitwise XOR between two binary numbers."""
        return bin(int(self.bin_number, 2) ^ int(other.bin_number, 2))[2:]

    def __invert__(self) -> str:
        """Does bitwise NOT binary number."""
        return "".join("1" if digit == "0" else "0" for digit in self.bin_number)

    def __str__(self) -> str:
        """Represents Binary Number without 0b."""
        return bin(int(self.bin_number, 2))[2:]


bin_1 = BinaryNumber("101")
bin_2 = BinaryNumber("11")

print(f"The bitwise AND operation between {bin_1} and {bin_2} is {bin_1 & bin_2}\n"
      f"The bitwise OR operation between {bin_1} and {bin_2} is {bin_1 | bin_2}\n"
      f"The bitwise XOR operation between {bin_1} and {bin_2} is {bin_1 ^ bin_2}\n"
      f"The bitwise NOT operation {bin_1} is {~bin_1}\n"
      f"The bitwise NOT operation {bin_2} is {~bin_2}\n")
