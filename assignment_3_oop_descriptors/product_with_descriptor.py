"""This module is designed for representation Product class with descriptor."""

from decimal import Decimal


class Descriptor:
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
        instance.__dict__[self.name] = value


class ProductWithDescriptor:
    """Represents the ProductWithDescriptor class with name of product and its price."""
    name = Descriptor()
    price = Descriptor()

    def __init__(self, name: str, price: float) -> None:
        """Initialize the ProductWithDescriptor class with name and price."""
        self.name = name
        self.price = Decimal(str(price))

    def __repr__(self):
        """Represents the Product class with name and price as a string."""
        return f"{self.name}: ${self.round_decimal(self.price)}"

    @staticmethod
    def round_decimal(price: Decimal) -> Decimal:
        """Rounds the price to two decimal places."""
        return price.quantize(Decimal("0.01"))


product_1 = ProductWithDescriptor("Doll", 10.2)
print(f"{product_1.name}: {product_1.price}\n"
      f"through __repr__\n{product_1}")
product_1.price = -10.1
