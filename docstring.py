def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)


square(5)
print(square.__doc__)

# Python docstrings are the string literals that appear right after the definition of a function, method, class, or module.
# if it not right after function defination then it is like comment

def add(num1, num2):
    """
    Add up two integer numbers.

    This function simply wraps the ``+`` operator, and does not
    do anything interesting, except for illustrating what
    the docstring of a very simple function looks like.

    Parameters
    ----------
    num1 : int
        First number to add.
    num2 : int
        Second number to add.

    Returns
    -------
    int
        The sum of ``num1`` and ``num2``.

    See Also
    --------
    subtract : Subtract one integer from another.

    Examples
    --------
    >>> add(2, 2)
    4
    >>> add(25, 0)
    25
    >>> add(10, -10)
    0
    """
    return num1 + num2
a=add(23,43)
print(add.__doc__)
