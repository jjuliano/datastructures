"""
Factorial of a positive integer -- https://en.wikipedia.org/wiki/Factorial
"""


def factorial(number: int) -> int:
    """
    Calculate the factorial of the specified number.

    >>> import math
    >>> all(factorial(i) == math.factorial(i) for i in range(20))
    True
    >>> factorial(0)
    1
    >>> factorial(1)
    1
    >>> factorial(5)
    120
    >>> factorial(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() only accepts integral values
    >>> factorial(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial() not defined for negative values
    """
    if number != int(number):
        raise ValueError("factorial() only accepts integral values")
    if number < 0:
        raise ValueError("factorial() not defined for negative values")
    value = 1
    for i in range(1, number + 1):
        value *= i
    return value


# Easy: factorial.easy, procedure Fact(n).
def factorial_recursive(number: int) -> int:
    """
    Calculate the factorial of a number using recursion.

    >>> import math
    >>> all(factorial_recursive(i) == math.factorial(i) for i in range(20))
    True
    >>> factorial_recursive(0)
    1
    >>> factorial_recursive(1)
    1
    >>> factorial_recursive(5)
    120
    >>> factorial_recursive(0.1)
    Traceback (most recent call last):
        ...
    ValueError: factorial_recursive() only accepts integral values
    >>> factorial_recursive(-1)
    Traceback (most recent call last):
        ...
    ValueError: factorial_recursive() not defined for negative values
    """
    # Not in Easy: Fact trusts its caller to pass a whole n >= 0.
    if not isinstance(number, int):
        raise ValueError("factorial_recursive() only accepts integral values")
    if number < 0:
        raise ValueError("factorial_recursive() not defined for negative values")
    # Easy Fact: if n = 0 then return(1)
    # Easy Fact: else return(n * Fact(n - 1))
    # Python also stops at 1, which saves the last call.
    return 1 if number in {0, 1} else number * factorial_recursive(number - 1)


if __name__ == "__main__":
    import doctest

    doctest.testmod()
    n = int(input("Enter a positive integer: ").strip() or 0)
    print(f"{n = } {factorial(n) = } {factorial_recursive(n) = }")
