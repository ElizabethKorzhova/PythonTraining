"""Module provides functions for working with numbers."""
import doctest


def is_even(n: int) -> bool:
    """
    Checks if the quotient of dividing the number n by two is equal to zero.
    :param n: integer number
    :return: True if n is even, False otherwise
    :raises TypeError: if n is not an integer

    >>> is_even(2)
    True
    >>> is_even(3)
    False
    """
    if not isinstance(n, int):
        raise TypeError('Number must be a integer')

    return n % 2 == 0


def get_factorial(n: int) -> int:
    """
    Calculates the factorial of n
    :param n: integer positive number
    :return: factorial of n
    :raises TypeError: if n is not an integer
    :raises ValueError: if n is negative

    >>> get_factorial(5)
    120
    >>> get_factorial(1)
    1
    >>> get_factorial(0)
    1
    >>> get_factorial(-1)
    Traceback (most recent call last):
    ...
    ValueError: Factorial doesn't exist for negative integers
    """
    if not isinstance(n, int):
        raise TypeError('Number must be a integer')
    if n < 0:
        raise ValueError("Factorial doesn't exist for negative integers")

    result = 1
    if n > 1:
        for i in range(2, n + 1):
            result *= i
    return result


if __name__ == '__main__':
    doctest.testmod()
