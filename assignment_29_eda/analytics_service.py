"""This module provides analytics service for order events."""
from typing import Dict, Any


class AnalyticsService:
    """Represents service that counts created and paid orders."""

    def __init__(self) -> None:
        """Initializes counters."""
        self.created_orders_count = 0
        self.paid_orders_count = 0

    def track_order_created(self, event_name: str, data: Dict[str, Any]) -> None:
        """Counts created order event."""
        self.created_orders_count += 1
        print(f"[ANALYTICS] Created orders: {self.created_orders_count}")

    def track_order_paid(self, event_name: str, data: Dict[str, Any]) -> None:
        """Counts paid order event."""
        self.paid_orders_count += 1
        print(f"[ANALYTICS] Paid orders: {self.paid_orders_count}")
