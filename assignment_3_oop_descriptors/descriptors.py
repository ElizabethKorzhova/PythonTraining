"""This module is designed to implement descriptors."""

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
