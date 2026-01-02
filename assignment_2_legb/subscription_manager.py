"""This module is designed for simulation newsletter subscription manager."""

from typing import Callable

subscribers = []


def subscribe(name: str) -> Callable[[], str]:
    """Function to subscribe a new subscriber."""
    subscribers.append(name)

    def confirm_subscription() -> str:
        """Function to confirm subscription with message."""
        return f"Subscription confirmed for {name}"

    return confirm_subscription


def unsubscribe(name: str) -> str:
    """Function to unsubscribe a subscriber."""
    if name in subscribers:
        subscribers.remove(name)
        return f"{name} successfully unsubscribed"
    return f"There is no subscriber {name}"


subscribe("Nick")
subscribe("Jack")
print(subscribers)
print(unsubscribe("Jack"))
print(subscribers)
print(unsubscribe("Marry"))
