"""This module is designed for simulation an order system with promotions."""

from typing import Callable

DISCOUNT = 0.1


def create_order(price: int | float) -> tuple[
    Callable[[], float],
    Callable[[int | float], None]
]:
    """Function to calculate the total price of the product."""
    final_price = price - (price * DISCOUNT)

    def apply_additional_discount(vip_discount: int | float) -> None:
        """Function to apply additional discount to price."""
        nonlocal final_price
        final_price = final_price - (final_price * vip_discount)
        print(f"Applied additional discount {vip_discount * 100}%")

    def get_final_price() -> float:
        """Function to get the final price."""
        return final_price

    return get_final_price, apply_additional_discount


get_price, set_additional_discount = create_order(1000)
print("Starting price: 1000\nFinal price with discount: ", get_price())
set_additional_discount(0.2)
print("Final price with all discounts: ", get_price())
