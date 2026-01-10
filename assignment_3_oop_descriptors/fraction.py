"""This module is designed for representation Fraction class using dunder methods."""

from __future__ import annotations
from math import gcd


class Fraction:
    """Class that represents Fraction in the form of numerator/denominator."""

    def __init__(self, numerator: int, denominator: int) -> None:
        """Initializes Fraction class with numerator and denominator."""
        if numerator < 0 and denominator < 0:
            numerator = abs(numerator)
            denominator = abs(denominator)

        common_divisor: int = gcd(numerator, denominator)
        self.numerator = numerator // common_divisor
        self.denominator = denominator // common_divisor

    def __add__(self, other: Fraction) -> Fraction:
        """Adds two Fractions together."""
        return Fraction(
            ((self.numerator * other.denominator) + (other.numerator * self.denominator)),
            self.denominator * other.denominator)

    def __sub__(self, other: Fraction) -> Fraction:
        """Subtracts two Fractions together."""
        return Fraction(
            ((self.numerator * other.denominator) - (other.numerator * self.denominator)),
            self.denominator * other.denominator)

    def __mul__(self, other: Fraction) -> Fraction:
        """Multiplies two Fractions together."""
        return Fraction(self.numerator * other.numerator, self.denominator * other.denominator)

    def __truediv__(self, other: Fraction) -> Fraction:
        """Divides two Fractions together."""
        return Fraction(self.numerator * other.denominator, self.denominator * other.numerator)

    def __repr__(self) -> str:
        """Represents numerical Fraction as a string."""
        return f"{self.numerator}/{self.denominator}"


if __name__ == "__main__":
    fraction_a = Fraction(-1, -4)
    fraction_b = Fraction(1, 2)

    print(f"Sum of {fraction_a} and {fraction_b} is {fraction_a + fraction_b}\n"
          f"Difference of {fraction_a} and {fraction_b} is {fraction_a - fraction_b}\n"
          f"Product of {fraction_a} and {fraction_b} is {fraction_a * fraction_b}\n"
          f"Quotient of {fraction_a} and {fraction_b} is {fraction_a / fraction_b}\n")
