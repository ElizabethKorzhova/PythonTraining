"""This module is designed for simulation products management in an online store.
In particular, the function of changing the price of the product and the function
of getting the information about product have been implemented."""

from typing import Callable


def create_product(name: str, price: float, quantity: int) -> tuple[
    Callable[[], dict[str, str | float | int]], Callable[[float], dict[str, str | float | int]]]:
    """Function to create a product with given name, price and quantity."""
    product: dict[str, str | int | float] = {
        "name": name,
        "price": price,
        "quantity": quantity
    }

    def change_price(new_price: float) -> dict[str, str | float | int]:
        """Function to change the price of the product."""
        product["price"] = new_price
        print(f"Price changed to {new_price}")
        return product

    def get_product() -> dict[str, str | float | int]:
        """Function to get the product information."""
        return product

    return get_product, change_price


get_product_info, set_new_price = create_product(name="Blue ball", price=100, quantity=10)
product_info = get_product_info()
print(
    f'Name product: {product_info["name"]}\nPrice product: {product_info["price"]}\n'
    f'Quantity product: {product_info["quantity"]}'
)
set_new_price(500)
