"""
Python Dictionaries

Dictionary

Dictionaries are used to store data values in key:value pairs.
A dictionary is a collection which is ordered, changeable and do not allow duplicates.

The keys can be numbers or strings and the values can be any data type.

Ordered or Unordered?

As of Python version 3.7, dictionaries are ordered. In Python 3.6 and earlier, dictionaries are unordered.

When we say that dictionaries are ordered, it means that the items have a defined order, and that order will not change.

Unordered means that the items do not have a defined order, you cannot refer to an item by using an index.

Changeable

Dictionaries are changeable, meaning that we can change, add or remove items after the dictionary has been created.
"""

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_active": False,
    "colors": ["red", "black", "purple"],
}

person_details = dict(name="John", age=36, country="USA")

print(person_details)
