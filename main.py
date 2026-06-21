"""
Python Decorators

Decorators let you add extra behavior to a function, without changing the function's code.

A decorator is a function that takes another function as input and returns a new function.
"""


def change_case(func):
    def wrapper():
        return func().upper()

    return wrapper


@change_case
def greet():
    return "Hello John."


result = greet()
print(result)

# changed_result = change_case(greet)
# print(changed_result())
