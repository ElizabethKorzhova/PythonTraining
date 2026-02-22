"""This script is designed to implement MutableClass which has methods for
dynamically adding and removing object attributes"""

from typing import Any


class MutableClass:
    """Represents an object that has methods for dynamically adding and removing attributes."""

    def add_attribute(self, name: str, value: Any) -> None:
        """Adds attribute with value to instance."""
        setattr(self, name, value)

    def remove_attribute(self, name: str) -> None:
        """Removes attribute with value from instance."""
        delattr(self, name)


if __name__ == '__main__':
    obj = MutableClass()

    obj.add_attribute("name", "Python")
    print(obj.name)

    obj.remove_attribute("name")
    print(obj.name)
