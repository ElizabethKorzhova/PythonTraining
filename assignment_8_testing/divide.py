"""Module provides divide function."""


def divide(a: int, b: int) -> float:
    """
    Divide two numbers.
    :param a: integer number (divided)
    :param b: integer number (divider)
    :return: result of division (float, quotient)
    :raises ZeroDivisionError: if divider is equal to 0
    :raises TypeError: if divided or/and divider is not an integer

    >>> divide(4, 2)
    2.0
    """
    if b == 0:
        raise ZeroDivisionError('Could not divide by zero')
    if not isinstance(b, int) or not isinstance(a, int):
        raise TypeError('divided and divider must be an integer')
    return a / b
