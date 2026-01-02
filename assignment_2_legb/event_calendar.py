"""This module is designed to develop simple event calendar where can
add, delete, and view events."""

from typing import Callable

events = []


def calendar() -> tuple[
    Callable[[str], None],
    Callable[[str], None],
    Callable[[], None],
]:
    """Function that returns tuple of functions for adding events to event calendar,
    removing events from event calendar and viewing events."""

    def add_event(event: str) -> None:
        """Function that adds events to event calendar and views events."""
        if event not in events:
            events.append(event)
            print(f"{event} added to event calendar")
        else:
            print(f"{event} has already added to event calendar")

    def remove_event(event: str) -> None:
        """Function that removes events from event calendar and views events."""
        if event in events:
            events.remove(event)
            print(f"{event} removed from event calendar")
        else:
            print(f"There is no {event} in event calendar")

    def view_events() -> None:
        """Function that views events from event calendar."""
        if not events:
            print("There is no upcoming events in event calendar")
        else:
            print("Upcoming events:")
            for event in events:
                print(event)

    return add_event, remove_event, view_events


add, remove, view = calendar()
view()
add("Meeting with Bob")
add("Meeting with Jack")
add("Meeting with Bob")
remove("Meeting with Bob")
remove("Meeting with Tom")
add("Meeting with Tom")
view()
