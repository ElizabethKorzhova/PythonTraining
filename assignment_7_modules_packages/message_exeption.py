"""Module provides custom exception MessageSendingException that raised
when messages won't be sent."""


class MessageSendingException(Exception):
    """Exception raised when messages won't be sent."""

    def __init__(self, service_name: str, details: str) -> None:
        """Initializes MessageSendingException class with service_name and details to
        insert into the exception."""
        self.service_name, self.details = service_name, details
        super().__init__(f"Error when sending message through {service_name}: {details}")
