"""This module provides order service that produces order events."""
from queue import Queue
from typing import Any, Tuple, Dict


class OrderService:
    """Represents service responsible for creating and paying orders."""

    def __init__(self, event_queue: Queue[Tuple[str, Dict[str, Any]]]) -> None:
        """Initializes order service."""
        self.event_queue = event_queue

    def create_order(self, order_id: int, user_email: str, amount: float) -> None:
        """Creates order and send order.created event to queue."""
        event_data = {
            "order_id": order_id,
            "user_email": user_email,
            "amount": amount,
        }

        self.event_queue.put(("order.created", event_data))

    def pay_order(self, order_id: int, phone_number: str) -> None:
        """Pays order and send order.paid event to queue."""
        event_data = {
            "order_id": order_id,
            "phone_number": phone_number,
        }

        self.event_queue.put(("order.paid", event_data))
