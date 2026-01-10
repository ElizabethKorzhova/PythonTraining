"""This module is designed for representation Product class with descriptor."""

from decimal import Decimal
from typing import Literal
from descriptors import Descriptor, CurrencyDescriptor


class ProductWithDescriptor:
    """Represents the ProductWithDescriptor class with name of product, its price and currency."""
    name = Descriptor()
    price = Descriptor()
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


if __name__ == "__main__":
    product_1 = ProductWithDescriptor("Doll", 10.2)
    print(f"{product_1.name}: {product_1.price} {product_1.currency}\n"
          f"\nshows through __repr__\n{product_1}\n")
    product_1.currency = "EUR"
    print(f"The currency has been changed to {product_1.currency}\n{product_1}\n")
    product_1.currency = "USD"
    print(f"The currency has been changed to {product_1.currency}\n{product_1}\n")
    product_1.price = -11.10
