"""This module is designed to represent User with first name and last name and email address
as well as to verify the correctness of the email."""

from descriptors import Descriptor, EmailDescriptor


class User:
    """Class that represents User with first name, last name and email address."""
    first_name = Descriptor()
    last_name = Descriptor()
    email = EmailDescriptor()

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Initializes User with first name, last name and email address."""
        self.first_name, self.last_name, self.email = first_name, last_name, email

    def __repr__(self):
        """Represents User with first name, last name and email address as a string."""
        return f"{self.first_name} {self.last_name}, {self.email}"


if __name__ == "__main__":
    user_1 = User("John", "Smith", "john@gmail.com")
    print(user_1)
    user_1.first_name = "Mike"
    user_1.last_name = "Miller"
    print(user_1)
    user_1.email = "m@@g.co"
