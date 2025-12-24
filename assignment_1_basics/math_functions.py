"""This module is designed for mathematical functions.
Presently it provides the function for calculating area of a circle. """
import math

def calculate_circle_area(radius: int|float) -> float:
    """Calculate the area of a circle given its radius."""
    return math.pi * radius ** 2
