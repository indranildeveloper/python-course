"""
Python Decorators

Decorator With Arguments

Decorators can accept their own arguments by adding another wrapper level.
"""

from functools import wraps


def change_case(num):
    def inner_func(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            """This is the wrapper function inside the decorator."""
            if num == 1:
                result = func(*args, **kwargs).upper()
            else:
                result = func(*args, **kwargs).lower()
            return result

        return wrapper

    return inner_func


@change_case(2)
def greet(name):
    """A simple function to greet John."""
    return f"Hello {name}."


@change_case
def greet_full_name(first_name, last_name):
    return f"Hello, {first_name} {last_name}."


result = greet("John")
print(result)
