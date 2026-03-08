"""Module provides Adapters for sending messages in a different way."""
from abstract_sender import MessageSender
from services import SMSService, EmailService, PushService


class SMSAdapter(MessageSender):
    """Class for sending messages through SMSService."""

    def __init__(self) -> None:
        """Initializes SMSAdapter."""
        self._sms_service = SMSService()

    def send_message(self, recipient: str, message: str) -> str:
        """Sends message to recipient through SMSService."""
        return self._sms_service.send_sms(recipient, message)


class EmailAdapter(MessageSender):
    """Class for sending messages through EmailService."""

    def __init__(self) -> None:
        """Initializes EmailAdapter."""
        self._email_service = EmailService()

    def send_message(self, recipient: str, message: str) -> str:
        """Sends message to recipient through EmailService."""
        return self._email_service.send_email(recipient, message)


class PushAdapter(MessageSender):
    """Class for sending messages through PushService."""

    def __init__(self) -> None:
        """Initializes PushAdapter."""
        self._push_service = PushService()

    def send_message(self, recipient: str, message: str) -> str:
        """Sends message to recipient through PushService."""
        return self._push_service.send_push(recipient, message)


if __name__ == '__main__':
    sms = SMSAdapter()
    print(sms.send_message("+380 066 000 00 00", "Hi!"))

    email = EmailAdapter()
    print(email.send_message("test@gmail.com", "Hi there!"))

    push = PushAdapter()
    print(push.send_message("device id", "Hello!"))
