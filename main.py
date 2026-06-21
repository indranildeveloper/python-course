"""
Python Decorators

Preserving Function Metadata
"""

from functools import wraps


def change_case(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        """This is the wrapper function inside the decorator."""
        return func(*args, **kwargs).upper()

    return wrapper


@change_case
def greet(name):
    """A simple function to greet John."""
    return f"Hello {name}."


@change_case
def greet_full_name(first_name, last_name):
    return f"Hello, {first_name} {last_name}."


print(greet.__name__)
print(greet.__doc__)

# def my_function():
#     """A simple function that returns Hello World."""
#     return "Hello World."


# print(my_function.__name__)
# print(my_function.__doc__)
