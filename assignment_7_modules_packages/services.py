"""Module provides classes for working with different services."""


class SMSService:
    """Class representing the SMS service."""

    @staticmethod
    def send_sms(phone_number: str, message: str) -> str:
        """Imitates sending message to phone number."""
        return f"Message to {phone_number} was sent.\nMessage: {message}\n"


class EmailService:
    """Class representing the email service."""

    @staticmethod
    def send_email(email_address: str, message: str) -> str:
        """Imitates sending email to email address."""
        return f"Email to {email_address} was sent.\nMessage: {message}\n"


class PushService:
    """Class representing the push service."""

    @staticmethod
    def send_push(device_id: str, message: str) -> str:
        """Imitates sending push message to device."""
        return f"Push to {device_id} was sent.\nMessage: {message}\n"
