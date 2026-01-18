"""This module is designed for representing simple BankAccount class and
custom exception InsufficientFundsException o handle in case of insufficient funds."""

from decimal import Decimal
from currency_converter import CurrencyConverter


class InsufficientFundsException(Exception):
    """Exception raised when insufficient funds occurs."""

    def __init__(self, required_amount: Decimal, current_balance: Decimal, currency: str = "USD",
                 transaction_type: str = "withdraw") -> None:
        """Initializes InsufficientFundsException class with required_amount, current_balance
        and currency to insert into the exception."""
        self.required_amount, self.current_balance = required_amount, current_balance
        self.currency, self.transaction_type = currency, transaction_type

        super().__init__(
            f"\nDECLINED Insufficient funds:\n\tbalance account: {current_balance:.2f}"
            f"{currency}\n\trequired amount: {required_amount:.2f}"
            f"{currency}\n\ttransaction type: {transaction_type}")


class BankAccount:
    """Class to represent a bank account."""

    def __init__(self, balance: str = "0", currency: str = "USD") -> None:
        """Initializes BankAccount class with private balance and currency attributes."""
        self.__balance = Decimal(balance)
        self.__currency = currency.upper()

    def transaction(self,
                    amount: str,
                    currency: str = "USD",
                    transaction_type: str = "withdraw"
                    ) -> None:
        """Simulates a bank account transaction."""
        amount = Decimal(amount)
        if self.__currency != currency.upper():
            converted_amount: float = CurrencyConverter().convert(
                float(amount), currency.upper(), self.__currency)
            amount = Decimal(str(converted_amount))
        if amount > self.__balance:
            raise InsufficientFundsException(
                amount, self.__balance, self.__currency, transaction_type
            )

        self.__balance -= amount
        print("Transaction successful!")

    def __repr__(self):
        """Represents BankAccount class with private balance and currency attributes as a string."""
        return f"Balance: {self.__balance:.2f} {self.__currency}"


if __name__ == "__main__":
    try:
        account = BankAccount("100", "EUR")
        account.transaction("50", "EUR")
        print(account)
        account.transaction("150", transaction_type="purchase")
        print(account)
    except InsufficientFundsException as ex:
        print(ex)
