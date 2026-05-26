"""
List Slicing

The general syntax for a slice is: list[start:stop:step]

It creates a copy of the list.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "cherry"]

fruits_copy = fruits[6:1:-1]

print(fruits_copy)
