"""
Python function documentation

Python docstrings (documentation strings) are string literals written directly below a function definition to explain what the function does.
"""

# print(print.__doc__)


# def divide(a, b):
#     """Divide two numbers safely.

#     Args:
#         a (int): The dividend.
#         b (int): The divisor.

#     Returns:
#         float: The quotient result.

#     Raises:
#         ValueError: If b equals zero.
#     """
#     if b == 0:
#         raise ValueError("Division by zero.")
#     return a / b


def divide(a, b):
    """
    Divide two numbers safely.

    Parameters
    ----------
    a : int
        The dividend.
    b : int
        The divisor.

    Returns
    -------
    float
    """
    return a / b
