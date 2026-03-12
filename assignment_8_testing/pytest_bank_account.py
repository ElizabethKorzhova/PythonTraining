"""Module for testing BankAccount class"""
from decimal import Decimal
from unittest.mock import MagicMock, patch

import requests
import pytest

from assignment_8_testing.bank_account import BankAccount


@pytest.fixture
def bank_account() -> BankAccount:
    """Fixture to initialize BankAccount class with starting balance for further tests.
    :return: instance of BankAccount class"""
    return BankAccount(100)


@pytest.mark.parametrize(("amount", "balance"), ((100.0, 200.0), (51.0, 151.0), (1, 101)))
def test_deposit_successes(bank_account: BankAccount, amount, balance) -> None:
    """
    Tests deposit method of BankAccount class for compliance of the expected result with the actual result.
    :param bank_account: instance of BankAccount class
    """
    bank_account.deposit(amount)
    account_balance = bank_account.get_balance()
    assert account_balance == pytest.approx(balance)


@pytest.mark.parametrize(("amount", "expected_exception"),
                         ((-100.0, ValueError), ("51", TypeError), (0, ValueError), (0.0, ValueError)))
def test_deposit_exceptions(bank_account: BankAccount, amount: int | float | str,
                            expected_exception: TypeError | ValueError) -> None:
    """
    Tests method deposit of BankAccount class for raises exceptions
    :param bank_account: instance of BankAccount class
    :param amount: not valid amount to raise exception
    :param expected_exception: expected exception type (ValueError or TypeError)
    """
    with pytest.raises(expected_exception):
        bank_account.deposit(amount)


@pytest.mark.parametrize("amount", (100, 10, 1.1, 50, 25.7, 100.0))
def test_withdraw_successes(bank_account: BankAccount, amount: int | float) -> None:
    """
    Tests method withdraw of BankAccount class for compliance of the expected result with the actual result.
    :param bank_account: instance of BankAccount class
    :param amount: amount of money to withdraw cash
    """
    expected_result = bank_account.get_balance() - Decimal(str(amount))
    bank_account.withdraw(amount)
    account_balance = bank_account.get_balance()
    assert account_balance == pytest.approx(expected_result)


@pytest.mark.parametrize(("amount", "expected_exception"),
                         (("34", TypeError), (200, ValueError), (100.01, ValueError), (-10, ValueError)))
def test_withdraw_exceptions(bank_account: BankAccount, amount: str | float | int,
                             expected_exception: ValueError | TypeError) -> None:
    """
    Tests method withdraw of BankAccount class for raises exceptions.
    :param bank_account: instance of BankAccount class
    :param amount: not valid amount to raise exception
    :param expected_exception: expected exception type (ValueError or TypeError)
    """
    with pytest.raises(expected_exception):
        bank_account.withdraw(amount)


@pytest.mark.parametrize(("amount", "expected_result"), ((100, 200), (1, 101), (10.1, 110.1), (50.01, 150.01)))
def test_get_balance_successes(bank_account: BankAccount, amount: int | float, expected_result: int | float) -> None:
    """
    Tests method get_balance of BankAccount class for compliance of the expected result with the actual result.
    :param bank_account: instance of BankAccount class
    :param amount: int or float positive number (amount of money)
    :param expected_result: expected amount of money
    """
    bank_account.deposit(amount)
    actual_result = bank_account.get_balance()
    assert actual_result == pytest.approx(Decimal(str(expected_result)))


@patch("requests.get")
def test_sync_balance_successful_response(mock_request: MagicMock, bank_account: BankAccount) -> None:
    """
    Tests method sync_balance of BankAccount class for getting successful response.
    :param mock_request: instance of MagicMock that patches requests.get
            and simulates the HTTP response from the bank API.
    :param bank_account: instance of BankAccount class
    """
    mock_response = MagicMock(status_code=200)
    mock_response.json.return_value = {"balance": 100.0}
    mock_request.return_value = mock_response
    bank_account.sync_balance()
    assert bank_account.get_balance() == Decimal(mock_response.json().get("balance"))


@patch("requests.get")
def test_sync_balance_failure_response(mock_request: MagicMock, bank_account: BankAccount) -> None:
    """
    Test method sync_balance of BankAccount class for getting failed response.
    :param mock_request: instance of MagicMock that patches requests.get
            and simulates the HTTP response from the bank API.
    :param bank_account: instance of BankAccount class
    """
    mock_response = MagicMock(status_code=403)
    mock_request.return_value = mock_response
    with pytest.raises(requests.exceptions.HTTPError):
        bank_account.sync_balance()


def test_empty_balance(bank_account: BankAccount) -> None:
    """
    Tests withdraw amount if the balance is not empty; otherwise skips this test
    :param bank_account: instance of BankAccount class
    """
    bank_account.withdraw(100)
    if not bank_account.get_balance():
        pytest.skip("Balance is empty")
    balance = bank_account.get_balance()
    bank_account.withdraw(10)
    assert bank_account.get_balance() == pytest.approx(balance - Decimal(str(10)))
