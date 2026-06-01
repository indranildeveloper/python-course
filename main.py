"""
Unpacking Dictionaries with **
"""


def greet(first_name, last_name):
    print(f"Hello there, {first_name} {last_name}")


person = {"first_name": "Sara", "last_name": "Smith"}
# greet(first_name="John", last_name="Doe")
greet(**person)  # greet(first_name="Sara", last_name="Smith")
