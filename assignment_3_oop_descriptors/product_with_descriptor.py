"""This module is designed for representation Product class with descriptor."""

from decimal import Decimal
from typing import Literal
from forex_python.converter import CurrencyRates

USD_RATE: float = CurrencyRates().get_rate("USD", "EUR")
EUR_RATE: float = CurrencyRates().get_rate("EUR", "USD")


class CurrencyDescriptor:
    """Represents the Descriptor for currency changing in ProductWithDescriptor class."""

    def __set_name__(self, owner, name: str) -> None:
        """Sets the name to attribute."""
        self.name = "__" + name

    def __get__(self, instance, owner) -> Decimal:
        """Gets attribute by the name."""
        return instance.__dict__[self.name]

    def __set__(self, instance, value: Literal["USD", "EUR"]) -> None:
        """Sets attribute by the name and change price."""
        prev_value: str | None = instance.__dict__.get(self.name)

        if prev_value == value:
            return

        if prev_value is not None:
            if prev_value == "USD" and value == "EUR":
                instance.price *= Decimal(str(USD_RATE))
            elif prev_value == "EUR" and value == "USD":
                instance.price *= Decimal(str(EUR_RATE))

        instance.__dict__[self.name] = value


class ProductDescriptor:
    """Represents the Descriptor for ProductWithDescriptor class."""

    def __set_name__(self, owner, name) -> None:
        """Sets the name to attributes."""
        self.name = "__" + name

    def __get__(self, instance, owner) -> str | Decimal:
        """Gets attribute by the name."""
        return instance.__dict__[self.name]

    def __set__(self, instance, value: float | str) -> None:
        """Sets attribute by the name."""
        if isinstance(value, str) and not value:
            raise ValueError("Name of a product must exist.")
        if isinstance(value, float) and value < 0:
            raise ValueError("Price cannot be negative.")
        if isinstance(value, float):
            instance.__dict__[self.name] = Decimal(str(value))
        else:
            instance.__dict__[self.name] = value


class ProductWithDescriptor:
    """Represents the ProductWithDescriptor class with name of product, its price and currency."""
    name = ProductDescriptor()
    price = ProductDescriptor()
    currency = CurrencyDescriptor()

    def __init__(self, name: str, price: float, currency: Literal["USD", "EUR"] = "USD") -> None:
        """Initialize the ProductWithDescriptor class with name, price and currency."""
        self.name = name
        self.price = price
        self.currency = currency

    def __repr__(self):
        """Represents the Product class with name, price and currency as a string."""
        return f"{self.name}: {self.round_decimal(self.price)} {self.currency}"

    @staticmethod
    def round_decimal(price: Decimal) -> Decimal:
        """Rounds the price to two decimal places."""
        return price.quantize(Decimal("0.01"))


product_1 = ProductWithDescriptor("Doll", 10.2)
print(f"{product_1.name}: {product_1.price} {product_1.currency}\n"
      f"\nshows through __repr__\n{product_1}\n")
product_1.currency = "EUR"
print(f"The currency has been changed to {product_1.currency}\n{product_1}\n")
product_1.currency = "USD"
print(f"The currency has been changed to {product_1.currency}\n{product_1}\n")
product_1.price = -11.10
