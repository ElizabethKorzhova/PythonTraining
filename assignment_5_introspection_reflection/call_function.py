"""This module is designed to implement call_function that call the corresponding
object method and return the result."""

from typing import Any


def call_function(obj: object, method_name: str, *args: Any) -> Any:
    """Calls the object method and returns the result."""
    try:
        return getattr(obj, method_name)(*args)
    except (AttributeError, TypeError) as ex:
        return f"Error: {ex}"
