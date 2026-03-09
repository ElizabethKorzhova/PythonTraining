"""Module represents the implementation of the Adapter pattern."""
import abc
from typing import List
from message_exeption import MessageSendingException


class MessageSender(abc.ABC):
    """Abstract class to send messages through different services."""

    @abc.abstractmethod
    def send_message(self, message: str) -> None:
        """Sends the given message."""
        pass

    @staticmethod
    def _check_data(service_name: str, name: str, value: str) -> None:
        """Checks if the given value in not empty."""
        if not value:
            raise MessageSendingException(service_name, f"{name} cannot be empty")


class SMSService:
    """Class to represent SMSService."""

    @staticmethod
    def send_sms(phone_number: str, message: str) -> None:
        """Sends the given message to phone number."""
        print(f"Sending SMS to {phone_number}: {message}")


class EmailService:
    """Class to represent EmailService."""

    @staticmethod
    def send_email(email_address: str, message: str) -> None:
        """Sends the given message to email address."""
        print(f"Sending the Email to {email_address}: {message}")


class PushService:
    @staticmethod
    def send_push(device_id: str, message: str) -> None:
        print(f"Sending the push notification to the device {device_id}: {message}")


class SMSAdapter(MessageSender):
    """Class to represent SMSAdapter."""

    def __init__(self, sms_service: SMSService, phone_number: str) -> None:
        """Initializes SMSAdapter class with sms_service and phone_number."""
        self.sms_service = sms_service
        self._check_data(sms_service.__class__.__name__, "phone number", phone_number)
        self.phone_number = phone_number

    def send_message(self, message: str) -> None:
        """Checks message and sends it to phone number."""
        self._check_data(self.sms_service.__class__.__name__, "message", message)
        self.sms_service.send_sms(self.phone_number, message)


class EmailAdapter(MessageSender):
    """Class to represent EmailAdapter."""

    def __init__(self, email_service: EmailService, email_address: str) -> None:
        """Initializes EmailAdapter class with email_service and email_address."""
        self.email_service = email_service
        self._check_data(email_service.__class__.__name__, "email address", email_address)
        self.email_address = email_address

    def send_message(self, message: str) -> None:
        """Checks message and sends it to email address."""
        self._check_data(self.email_service.__class__.__name__, "message", message)
        self.email_service.send_email(self.email_address, message)


class PushAdapter(MessageSender):
    """Class to represent PushAdapter."""

    def __init__(self, push_service: PushService, device_id: str) -> None:
        """Initializes PushAdapter class with push_service and device_id."""
        self.push_service = push_service
        self._check_data(push_service.__class__.__name__, "device id", device_id)
        self.device_id = device_id

    def send_message(self, message: str) -> None:
        """Checks message and sends it to push address."""
        self._check_data(self.push_service.__class__.__name__, "message", message)
        self.push_service.send_push(self.device_id, message)


class MessageSystem:
    """Class to represent MessageSystem class for sending messages through all given services.

    Public methods:
        send_via_all_services(message):
            sends message through all available services.
    """

    def __init__(self, services_list: List) -> None:
        """Initializes MessageSystem class with services_list."""
        self._services_list = services_list

    def send_via_all_services(self, message: str) -> None:
        """Sends message through all available services.
        If the message was not sent successfully, its handles the MessageSendingException."""
        for service in self._services_list:
            try:
                service.send_message(message)
            except MessageSendingException as exception:
                print(exception)


if __name__ == '__main__':
    sms = SMSService()
    email = EmailService()
    push = PushService()

    sms_adapter = SMSAdapter(sms, "+380123456789")
    email_adapter = EmailAdapter(email, "user@example.com")
    push_adapter = PushAdapter(push, "device123")

    services = [sms_adapter, email_adapter, push_adapter]

    message_system = MessageSystem(services)

    message_sample = "Hello! This is a test message."

    message_system.send_via_all_services(message_sample)
