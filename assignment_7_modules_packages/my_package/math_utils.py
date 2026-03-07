"""This module provides utility functions for math manipulation."""
__all__ = ["factorial"]


def factorial(number: int) -> int:
    """Calculates the factorial of a given number"""
    temp_factorial = 1
    for num in range(2, number + 1):
        temp_factorial *= num
    return temp_factorial
