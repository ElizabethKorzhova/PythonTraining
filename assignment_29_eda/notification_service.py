"""This module provides notification event listeners."""
from typing import Any, Dict


def send_order_created_email(event_name: str, data: Dict[str, Any]) -> None:
    """Sends email when order is created."""
    print(f"[EMAIL] Order #{data['order_id']} was created. "
          f"Email sent to {data['user_email']}.")


def send_order_paid_sms(event_name: str, data: Dict[str, Any]) -> None:
    """Sends SMS when order is paid."""
    print(f"[SMS] Order #{data['order_id']} was paid. "
          f"SMS sent to {data['phone_number']}.")
