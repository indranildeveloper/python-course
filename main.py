"""
Python Functions

Positional Arguments

When you call a function with arguments without using keywords, they are called positional arguments.
Positional arguments must be in the correct order.

Keyword Arguments

You can send arguments with the key = value syntax.
This way, with keyword arguments, the order of the arguments does not matter.
The phrase Keyword Arguments is often shortened to kwargs in Python documentation.
"""


def get_full_name(first_name="Sara", last_name="Smith"):
    print(f"Your full name is: {first_name} {last_name}")


get_full_name("John", "Doe")
get_full_name(first_name="Jane", last_name="Doe")
get_full_name()
