"""
Python - List Comprehension

List comprehension offers a shorter syntax when you want to create a new list based on the values of an existing list.

The Syntax
newlist = [expression for item in iterable if condition == True]
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

fruits_upper = []

for fruit in fruits:
    fruits_upper.append(fruit.upper())

fruits_upper = [fruit.upper() for fruit in fruits]

print(fruits)
print(fruits_upper)
