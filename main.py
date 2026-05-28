"""
Python Dictionaries

Python Dictionary pop() Method
The pop() method removes the specified item from the dictionary.

Python Dictionary popitem() Method
The popitem() method removes the item that was last inserted into the dictionary. In versions before 3.7, the popitem() method removes a random item.

Python Dictionary update() Method
The update() method inserts the specified items to the dictionary.
"""

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_active": False,
}

popped_value = car_details.pop("model")
popped_value = car_details.popitem()
print(popped_value)

car_color = {"color": "red"}

car_details.update(car_color)

print(car_details)
