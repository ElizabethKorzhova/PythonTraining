"""This module is designed for representation Price class with the possibility
of rounding to two decimal places. This class will be used in the future PaymentGateway class
to process financial transactions."""

from __future__ import annotations
from decimal import Decimal


class Price:
    """Represents the price of the product."""

    def __init__(self, price: str) -> None:
        """Initializes the price."""
        if Decimal(price) < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = self.round_decimal(Decimal(price))

    @property
    def price(self) -> Decimal:
        """Returns the price of the product."""
        return self.__price

    @price.setter
    def price(self, price: str) -> None:
        """Sets the price of the product."""
        self.__price = self.round_decimal(Decimal(price))

    def __add__(self, other: Price) -> Price:
        """Adds two prices."""
        return Price(str(self.__price + other.price))

    def __sub__(self, other: Price) -> Price:
        """Subtracts two prices."""
        if (self.__price - other.price) < 0:
            raise ValueError("Cannot perform subtraction.")
        return Price(str(self.__price - other.price))

    def __lt__(self, other: Price) -> bool:
        """Checks if the price is less than other price."""
        return self.__price < other.price

    def __gt__(self, other: Price) -> bool:
        """Checks if the price is greater than other price."""
        return self.__price > other.price

    def __eq__(self, other: object) -> bool:
        """Checks if the price of two products are equal. """
        if not isinstance(other, Price):
            return NotImplemented
        return self.__price == other.price

    def __repr__(self) -> str:
        """Represents Price as a string with rounding to two decimal places."""
        return f"${self.__price}"

    @staticmethod
    def round_decimal(price: Decimal) -> Decimal:
        """Rounds the price to two decimal places."""
        return price.quantize(Decimal("0.01"))


if __name__ == "__mail__":
    price_1 = Price("0.1")
    price_2 = Price("0.2")
    print(f"Sum of {price_1} and {price_2} is {price_1 + price_2}\n"
          f"Difference of {price_2} and {price_1} is {price_2 - price_1}\n"
          f"Is {price_1} less than {price_2}? {price_1 < price_2}\n"
          f"Is {price_1} greater than {price_2}? {price_1 > price_2}\n"
          f"Are {price_1} and {price_2} equal? {price_1 == price_2}\n")
