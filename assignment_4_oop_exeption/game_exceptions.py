"""This module is designed for representing custom exceptions for the game."""


class GameEventException(Exception):
    """Exception raised when game event occurs."""

    def __init__(self, event_type: str, details: dict) -> None:
        """Initializes GameEventException class with event_type and details to
        insert into the exception."""
        self.event_type, self.details = event_type, details
        formatted_details = "\n\t".join(
            f"{key}: {value}" for key, value in details.items()
        )

        super().__init__(f"{event_type}\n\t{formatted_details}")


class InsufficientResourcesException(Exception):
    """Exception raised when resources are not sufficient."""

    def __init__(self, required_resource, required_amount, current_amount) -> None:
        """Initializes InsufficientResourcesException class with required_resource,
        required_amount and current_amount to insert into the exception."""
        self.required_resource = required_resource
        self.required_amount = required_amount
        self.current_amount = current_amount

        super().__init__(
            f"\nInsufficient resources: you need collect {required_amount - current_amount} "
            f"more {required_resource}"
        )
