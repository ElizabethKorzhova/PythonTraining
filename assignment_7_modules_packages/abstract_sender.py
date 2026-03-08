"""Module provides abstract class MessageSender for service Adapters."""
import abc


class MessageSender(abc.ABC):
    """Class representing MessageSender abstract class."""

    @abc.abstractmethod
    def send_message(self, recipient: str, message: str) -> str:
        """Sends message."""
        pass
