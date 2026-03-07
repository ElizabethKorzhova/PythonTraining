"""Main module is designed to test the functions of the modules."""

from .math_utils import factorial
from .string_utils import to_lower_case, remove_spaces

if __name__ == '__main__':
    print(f"Factorial of 1: {factorial(1)}\n"
          f"Factorial of 10: {factorial(10)}\n"
          f"\nTest to_lower_case_function: {to_lower_case('HELLO')}\n"
          f"Test remove_spaces function: {remove_spaces('   Hello ')}")
