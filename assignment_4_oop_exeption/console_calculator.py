"""This module is designed for representing console calculator that
performs basic arithmetic operations."""

from __future__ import annotations

ALLOWED_OPERATIONS: list[str] = ["+", "-", "*", "/", "e"]


def check_operation(operation: str) -> None:
    """Checks if the given operation is allowed."""
    if operation not in ALLOWED_OPERATIONS:
        raise UnknownOperationError(operation)


class UnknownOperationError(Exception):
    """Exception raised when an unknown operation occurs."""

    def __init__(self, operation: str) -> None:
        """Initializes UnknownOperationError class with operation to insert into the exception."""
        self.operation = operation
        super().__init__(f"Operation {operation} not allowed.")


class Integer:
    """Class that represents Integer number."""

    def __init__(self, number: int) -> None:
        """Initializes Integer class with given number."""
        self.__number = number

    @property
    def number(self) -> int:
        """Gets private number attribute."""
        return self.__number

    def __add__(self, other: Integer) -> int:
        """Adds two numbers."""
        return self.__number + other.number

    def __sub__(self, other: Integer) -> int:
        """Subtracts two numbers."""
        return self.__number - other.number

    def __mul__(self, other: Integer) -> int:
        """Multiplies two numbers."""
        return self.__number * other.number

    def __truediv__(self, other: Integer) -> float:
        """Divides two numbers."""
        if other.number == 0:
            raise ZeroDivisionError("Cannot divide by zero")
        return self.__number / other.number


if __name__ == "__main__":
    while True:
        try:
            operation_choice: str = input(
                "Choose the one option below:\n\tadd numbers (+)\n\tsubtrack numbers (-)"
                "\n\tmultiply numbers (*)\n\tdivide numbers (/)\n\texit (e) >>> ")
            check_operation(operation_choice)

            if operation_choice == "e":
                print("\nCalculator closed.")
                break

            first_number: int = int(input("Enter first number: "))
            second_number: int = int(input("Enter second number: "))

            if operation_choice == "+":
                print(f"Result: {Integer(first_number) + Integer(second_number)}\n")

            if operation_choice == "-":
                print(f"Result: {Integer(first_number) - Integer(second_number)}\n")

            if operation_choice == "*":
                print(f"Result: {Integer(first_number) * Integer(second_number)}\n")

            if operation_choice == "/":
                print(f"Result: {Integer(first_number) / Integer(second_number)}\n")

        except UnknownOperationError as ex:
            print(f"\n{ex}\n")

        except ValueError as ex:
            print(f"\nNumber must be an integer: {ex}\n")

        except ZeroDivisionError as ex:
            print(f"\n{ex}\n")
