"""This script is designed to test call_function."""

from assignment_5_introspection_reflection.call_function import call_function


# pylint: disable=invalid-name
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
