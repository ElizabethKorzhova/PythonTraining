"""This module is designed for demonstration of the use of built-in functions
and their override with local functions"""

test_data = [1, 2, 3, 5, 8]


def my_sum() -> str:
    """Function that override built-in sum function and return string"""
    global sum
    sum = my_sum
    return "This is my custom sum function!"


print(sum(test_data))
print(my_sum())
print(sum())
