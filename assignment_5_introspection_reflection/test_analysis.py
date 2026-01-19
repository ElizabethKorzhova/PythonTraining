"""This script is designed to test analyze_object function."""

from analyze_object import analyze_object


# pylint: disable=too-few-public-methods
class MyClass:
    """This class is designed to test analyze_object function."""

    def __init__(self, value):
        """Initializes MyClass with value."""
        self.value = value

    def say_hello(self):
        """Returns message with value."""
        return f"Hello, {self.value}"


obj = MyClass("World")
analyze_object(obj)
