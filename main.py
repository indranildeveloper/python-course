"""
Python - List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

The Syntax
newlist = [expression for item in iterable if condition == True]
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]
# fruits_new = []

# for fruit in fruits:
#     if "a" in fruit:
#         fruits_new.append(fruit)

# fruits_new = [fruit for fruit in fruits if "a" in fruit]

fruits_new = [fruit if fruit != "banana" else "orange" for fruit in fruits]

print(fruits_new)
