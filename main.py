"""
Python Dictionaries

Python Dictionary clear() Method
The clear() method removes all the elements from a dictionary.

Python Dictionary copy() Method
The copy() method returns a copy of the specified dictionary.

Python Dictionary fromkeys() Method
The fromkeys() method returns a dictionary with the specified keys and the specified value.

Python Dictionary get() Method
The get() method returns the value of the item with the specified key.
"""

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_active": False,
    "colors": ["red", "black", "purple"],
}

print(car_details["brand"])
print(car_details.get("abc"))

# car_details.clear()

# car_details_copy = car_details.copy()
# print(car_details is car_details_copy)

# x = ["key1", "key2", "key3"]
# y = 0

# demo_dictionary = dict.fromkeys(x, y)
# print(demo_dictionary)
