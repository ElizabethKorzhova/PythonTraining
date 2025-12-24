"""This module provides a simple class to represent a rectangle."""


class Rectangle:
    """Represent the Rectangle with a width and a height."""

    def __init__(self, width: int|float, height: int|float) -> None:
        """Initialize the Rectangle with the width and height."""
        self.__width = width
        self.__height = height

    @property
    def width(self) -> int|float:
        """Get the width of the rectangle."""
        return self.__width

    @property
    def height(self) -> int|float:
        """Get the height of the rectangle."""
        return self.__height

    def area(self) -> int|float:
        """Calculate the area of the rectangle."""
        return self.__width * self.__height

    def perimeter(self) -> int|float:
        """Calculate the perimeter of the rectangle."""
        return 2 * (self.__width + self.__height)

    def is_square(self) -> bool:
        """Check if the rectangle is square."""
        return self.__width == self.__height

    def resize(self, new_width: int|float, new_height: int|float) -> None:
        """Resize the rectangle to a new width and height."""
        self.__width = new_width
        self.__height = new_height
