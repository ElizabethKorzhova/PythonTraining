"""This script is designed to implement call_function that call the corresponding
object method and return the result."""

from typing import Any


def call_function(obj: object, method_name: str, *args: Any) -> Any:
    """Calls the object method and returns the result."""
    try:
        return getattr(obj, method_name)(*args)
    except (AttributeError, TypeError) as ex:
        return f"Error: {ex}"


if __name__ == '__main__':
    class Calculator:
        """Class that represent simple calculator function."""

        def add(self, a, b):
            """Add two parameters."""
            return a + b

        def subtract(self, a, b):
            """Subtract two parameters."""
            return a - b


    calc = Calculator()
    print(call_function(calc, "add", 10, 5))
    print(call_function(calc, "subtract", 10, 5))
