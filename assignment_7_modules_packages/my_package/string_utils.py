"""This module provides utility functions for string manipulation."""
__all__ = ["to_lower_case", "remove_spaces"]


def to_lower_case(string: str) -> str:
    """Returns the string where all characters are lower case."""
    return string.lower()


def remove_spaces(string: str) -> str:
    """Removes any leading, and trailing whitespaces.."""
    return string.strip()
