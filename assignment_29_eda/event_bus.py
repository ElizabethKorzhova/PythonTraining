"""This module provides custom EventBus implementation."""

from collections import defaultdict
from typing import Any, Callable, Dict, List

EventCallback = Callable[[str, Dict[str, Any]], None]


class EventBus:
    """Represents custom event bus with subscriptions and event logging."""

    def __init__(self) -> None:
        """Initializes subscribers and event log."""
        self._subscribers: Dict[str, List[EventCallback]] = defaultdict(list)
        self.event_log: List[Dict[str, Any]] = []

    def subscribe(self, event_name: str, callback: EventCallback) -> None:
        """Subscribes callback to event."""
        if callback not in self._subscribers[event_name]:
            self._subscribers[event_name].append(callback)

    def unsubscribe(self, event_name: str, callback: EventCallback) -> None:
        """Unsubscribes callback from event."""
        if callback in self._subscribers[event_name]:
            self._subscribers[event_name].remove(callback)

    def emit(self, event_name: str, data: Dict[str, Any]) -> None:
        """
        Emit event and notify all listeners.

        Args:
            event_name: Event name.
            data: Event payload.
        """
        self.event_log.append({"event_name": event_name, "data": data})

        for callback in self._subscribers[event_name]:
            callback(event_name, data)