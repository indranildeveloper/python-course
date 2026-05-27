"""
Python Dictionaries

Accessing Items

You can access the items of a dictionary by referring to its key name, inside square brackets.
There is also a method called get() that will give you the same result.

Get Keys
The keys() method will return a list of all the keys in the dictionary.

Get Values
The values() method will return a list of all the values in the dictionary.

Get Items
The items() method will return each item in a dictionary, as tuples in a list.
"""

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_active": False,
    "colors": ["red", "black", "purple"],
}

print(car_details["is_active"])
print(car_details.get("is_active"))
print(car_details.keys())
print(car_details.values())
print(car_details.items())
