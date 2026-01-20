"""This module is designed to implement create_class function that creates a class
with the given name and methods"""

from typing import Callable


def create_class(class_name: str, methods: dict[str, Callable]) -> type:
    """Returns created class."""
    return type(class_name, (object,), methods)
