"""This module is designed to implement the calculator."""

from typing import Literal, Callable


def create_calculator(operation: Literal["+", "-", "*", "/"]) -> Callable[
    [int | float, int | float], int | float
]:
    """Function to create the calculator that calculates sum, difference,
    quotient and product of two numbers."""
    if operation == "+":
        return lambda a, b: a + b
    if operation == "-":
        return lambda a, b: a - b
    if operation == "*":
        return lambda a, b: a * b
    return lambda a, b: a / b


number_1 = 2
number_2 = 3

print(f"Sum of {number_1} and {number_2}: {create_calculator('+')(number_1, number_2)}\n"
      f"Difference of {number_1} and {number_2}: {create_calculator('-')(number_1, number_2)}\n"
      f"Product of {number_1} and {number_2}: {create_calculator('*')(number_1, number_2)}\n"
      f"Quotient of {number_1} and {number_2}: {create_calculator('/')(number_1, number_1)}\n")
