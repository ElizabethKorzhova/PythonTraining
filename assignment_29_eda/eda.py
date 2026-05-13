"""This module provides Event-driven architecture example with custom EventBus."""
from collections import defaultdict
from typing import Any, Callable, Dict, List

EventCallback = Callable[[str, Dict[str, Any]], None]


class EventBus:
    """Represents custom event bus with subscriptions, wildcard support and event logging."""

    def __init__(self) -> None:
        """Initializes subscribers storage and event log."""
        self._subscribers: Dict[str, List[EventCallback]] = defaultdict(list)
        self.event_log: List[Dict[str, Any]] = []

    def subscribe(self, event_name: str, callback: EventCallback) -> None:
        """Subscribes callback to a specific event or wildcard event."""
        if callback not in self._subscribers[event_name]:
            self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: EventCallback) -> None:
        """Unsubscribes callback from event."""
        if callback in self._subscribers[event_name]:
            self._subscribers[event_name].remove(callback)

    def emit(self, event_name: str, data: Dict[str, Any]) -> None:
        """Emit event and call all matching listeners."""
        self._log_event(event_name, data)

        for subscribed_event, callbacks in self._subscribers.items():
            if self._is_event_match(subscribed_event, event_name):
                for callback in callbacks:
                    callback(event_name, data)

    def _log_event(self, event_name: str, data: Dict[str, Any]) -> None:
        """Adds emitted event to event log."""
        self.event_log.append(
            {
                "event_name": event_name,
                "data": data,
            }
        )

    @staticmethod
    def _is_event_match(subscribed_event: str, emitted_event: str) -> bool:
        """Checks if subscribed event matches emitted event."""
        if subscribed_event == emitted_event:
            return True

        if subscribed_event.endswith(".*"):
            prefix = subscribed_event.removesuffix(".*")
            return emitted_event.startswith(f"{prefix}.")

        return False


def email_sender(event_name: str, data: Dict[str, Any]) -> None:
    """Sends email notification for user events."""
    print(f"[EMAIL] Event: {event_name}. Data: {data}")


def logger(event_name: str, data: Dict[str, Any]) -> None:
    """Logs event information."""
    print(f"[LOGGER] Event: {event_name}. Data: {data}")


def analytics(event_name: str, data: Dict[str, Any]) -> None:
    """Tracks event in analytics system."""
    print(f"[ANALYTICS] Event: {event_name}. Data: {data}")


if __name__ == "__main__":
    bus = EventBus()

    bus.subscribe("user.registered", email_sender)
    bus.subscribe("user.*", logger)
    bus.subscribe("order.created", analytics)

    bus.emit(
        "user.registered",
        {
            "user_id": 1,
            "email": "user@example.com",
        },
    )

    bus.emit(
        "user.deleted",
        {
            "user_id": 1,
        },
    )

    bus.emit(
        "order.created",
        {
            "order_id": 100,
            "amount": 250,
        },
    )

    print("\nEvent log:")
    for event in bus.event_log:
        print(event)
