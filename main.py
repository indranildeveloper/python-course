"""
Python Decorators

Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
"""


def change_case(func):
    def wrapper(*args, **kwargs):
        return func(*args, **kwargs).upper()

    return wrapper


@change_case
def greet(name):
    return f"Hello {name}."


@change_case
def greet_full_name(first_name, last_name):
    return f"Hello, {first_name} {last_name}."


result = greet("John")
result_full_name = greet_full_name("Jane", "Doe")

print(result)
print(result_full_name)
