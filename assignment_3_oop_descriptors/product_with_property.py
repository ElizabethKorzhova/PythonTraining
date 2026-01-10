"""This module is designed for representation Product class with getter and setter
using built-in decorators."""

from decimal import Decimal


class ProductWithProperty:
    """Represents the ProductWithProperty class with name of product and its price."""

    def __init__(self, name: str, price: float) -> None:
        """Initialize the ProductWithProperty class with name and price."""
        if Decimal(str(price)) < 0:
            raise ValueError("Price cannot be negative.")

        if not name:
            raise ValueError("Name of a product must exist.")

        self.__name = name
        self.__price = Decimal(str(price))

    @property
    def name(self) -> str:
        """Gets the name of the product."""
        return self.__name

    @name.setter
    def name(self, name: str) -> None:
        """Sets the name of the product."""
        if not name:
            raise ValueError("Name of a product must exist.")
        self.__name = name

    @property
    def price(self) -> Decimal:
        """Gets the price of the product."""
        return self.round_decimal(self.__price)

    @price.setter
    def price(self, price: float) -> None:
        """Sets the price of the product."""
        if Decimal(str(price)) < 0:
            raise ValueError("Price cannot be negative.")
        self.__price = Decimal(str(price))

    def __repr__(self):
        """Represents the Product class with name and price as a string."""
        return f"{self.__name}: ${self.round_decimal(self.__price)}"

    @staticmethod
    def round_decimal(price: Decimal) -> Decimal:
        """Rounds the price to two decimal places."""
        return price.quantize(Decimal("0.01"))


product_1 = ProductWithProperty("Doll", 10.2)
print(f"{product_1.name}: {product_1.price}\n"
      f"through __repr__\n{product_1}")
product_1.price = -10.1
