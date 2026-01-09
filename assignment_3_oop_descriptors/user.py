"""This module is designed to represent User with first name and last name and email address
as well as to verify the correctness of the email."""

import re


class User:
    """Class that represents User with first name, last name and email address."""

    def __init__(self, first_name: str, last_name: str, email: str) -> None:
        """Initializes User with first name, last name and email address."""
        if not self.is_valid_email(email):
            raise ValueError("Email address is not valid.")
        self.__first_name, self.__last_name, self.__email = first_name, last_name, email

    def __repr__(self):
        """Represents User with first name, last name and email address as a string."""
        return f"{self.first_name} {self.last_name}, {self.email}"

    @property
    def first_name(self) -> str:
        """Gets first name."""
        return self.__first_name

    @property
    def last_name(self) -> str:
        """Gets last name."""
        return self.__last_name

    @property
    def email(self) -> str:
        """Gets email address."""
        return self.__email

    @first_name.setter
    def first_name(self, first_name: str) -> None:
        """Sets first name."""
        self.__first_name = first_name

    @last_name.setter
    def last_name(self, last_name: str) -> None:
        """Sets last name."""
        self.__last_name = last_name

    @email.setter
    def email(self, email: str) -> None:
        """Sets email address."""
        if self.is_valid_email(email):
            self.__email = email
        else:
            raise ValueError("Email address is not valid.")

    @staticmethod
    def is_valid_email(email_to_check: str) -> bool:
        """Checks if email is valid."""
        regex = r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,7}"
        return bool(re.fullmatch(regex, email_to_check))


user_1 = User("John", "Smith", "john@gmail.com")
print(user_1)
user_1.first_name = "Mike"
user_1.last_name = "Miller"
print(user_1)
user_1.email = "m@@g.co"
