"""This module is designed for developing memoize decorator for functions of
calculating factorial number and fibonacci number.
Functions to calculate factorial number and fibonacci number (recursion) have been developed.
"""


def memoize(function):
    """Decorator for caching results of given function."""
    cache = {}

    def wrapper(args):
        if args not in cache:
            cache[args] = function(args)
        return cache[args]

    return wrapper


@memoize
def factorial(num: int) -> int:
    """Function to calculate factorial number."""
    result = 1
    for number in range(1, num + 1):
        result *= number
    return result


@memoize
def fibonacci(num: int) -> int:
    """Function to calculate fibonacci number."""
    if num <= 0:
        return 0
    if num == 1:
        return 1
    return fibonacci(num - 1) + fibonacci(num - 2)


print("The value of factorial of 10:", factorial(10))
print("The value of factorial of 6:", factorial(6))

print("\nFibonacci sequence:")
for i in range(20):
    print(fibonacci(i), end=" ")
