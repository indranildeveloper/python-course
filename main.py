"""
Python Higher Order Functions

A higher-order function (HOF) in Python is a function that either accepts one or more functions as arguments or returns a function as its output.
"""

# def greet(name):
#     return f"Hello, {name}"


# def formal_greeting(func, user_name):
#     return func(user_name).upper()


# print(formal_greeting(greet, "John"))


def multiplier(factor):
    def multiply_by(number):
        return number * factor

    return multiply_by


double = multiplier(2)
print(double(10))
