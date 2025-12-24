"""
This module is designed for testing the functionality of the Rectangle class and
correctness of work calculate_circle_area function
"""

from rectangle import Rectangle
from math_functions import calculate_circle_area

# test subtask 1
print("The area of the circle is: ",
      calculate_circle_area(float(input("Enter the radius of the circle: "))))

# test subtask 2
rectangle_abcd = Rectangle(10.4, 7.9)
print(f"\nThe rectangle with the width of {rectangle_abcd.width} and the height "
      f"of {rectangle_abcd.height}")
print("The area of the rectangle is: ", rectangle_abcd.area())
print("The perimeter of the rectangle is: ", rectangle_abcd.perimeter())
print("Is the rectangle the square? ", rectangle_abcd.is_square())
rectangle_abcd.resize(25, 25)
print(f"The width and the height of the rectangle were changed to {rectangle_abcd.width} "
      f"and {rectangle_abcd.height} respectively")
print("Is the rectangle a square?", rectangle_abcd.is_square())
