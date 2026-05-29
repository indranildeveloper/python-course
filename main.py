"""
Python Set Methods

Access Set Items

You cannot access items in a set by referring to an index or a key.
But you can loop through the set items using a for loop, or ask if a specified value is present in a set, by using the in keyword.
"""

fruits_set = {"apple", "orange", "banana", "cherry"}

for fruit in fruits_set:
    print(fruit)

print("apple" in fruits_set)
