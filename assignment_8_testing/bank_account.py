"""Module provides BankAccount class."""
from decimal import Decimal
import requests


class BankAccount:
    """Class represents BankAccount."""
    __BANK_API_URL = ""

    def __init__(self, balance: float | int) -> None:
        """
        Initializes BankAccount class.
        :param balance: float or integer number (amount of money on bank account)
        """
        self.__check_amount(balance)
        self.__balance = Decimal(str(balance))

    def deposit(self, amount: float | int) -> None:
        """
        Deposit amount to bank account.
        :param amount: float or integer positive number (amount of money)
        """
        self.__check_amount(amount)
        self.__balance += Decimal(str(amount))

    def withdraw(self, amount: float) -> None:
        """
        Withdraw cash from bank account.
        :param amount: float or integer positive number (amount of money)
        :raise: ValueError if amount is less than balance of bank account
        """
        self.__check_amount(amount)
        if self.__balance < Decimal(str(amount)):
            raise ValueError("Insufficient funds in your bank account")
        self.__balance -= Decimal(str(amount))

    def get_balance(self) -> Decimal:
        """
        Returns balance of bank account
        :return: balance in Decimal type with two decimal places
        :raise ConnectionError: if the status code of response is not 200
        """
        return self.__balance.quantize(Decimal("0.01"))

    def sync_balance(self) -> None:
        """Imitates connection to bank API and stores balance of bank account."""
        response = requests.get(self.__BANK_API_URL)
        if response.status_code != 200:
            raise requests.exceptions.HTTPError(
                f"Failed to get data from bank account: status code {response.status_code}")
        data = response.json()
        self.__balance = Decimal(str(data["balance"]))

    @staticmethod
    def __check_amount(amount: float) -> None:
        """
        Checks if amount is positive and type of amount is float.
        :param amount: float number (amount of money)
        :raises ValueError: if amount is less or equal to zero
        :raises TypeError: if amount is not a float
        """
        if not isinstance(amount, (float, int)):
            raise TypeError(f"Amount must be a float or int, not {type(amount)}")
        if amount <= 0:
            raise ValueError("Amount must be positive")
