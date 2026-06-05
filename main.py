"""
The __name__ variable
"""

from greet import greet


def say_hello():
    print(f"Inside the main module and the __name__ is {__name__}")


say_hello()
greet()
