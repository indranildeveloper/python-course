"""
Python Tuples

Tuples are used to store multiple items in a single variable.
A tuple is a collection which is ordered and immutable/unchangeable.

Tuple Items

Tuple items are ordered, unchangeable, and allow duplicate values.
Tuple items are indexed, the first item has index [0], the second item has index [1] etc.

Ordered

When we say that tuples are ordered, it means that the items have a defined order, and that order will not change.

Unchangeable

Tuples are unchangeable, meaning that we cannot change, add or remove items after the tuple has been created.

Allow Duplicates

Since tuples are indexed, they can have items with the same value.

Create Tuple With One Item

To create a tuple with only one item, you have to add a comma after the item, otherwise Python will not recognize it as a tuple.
"""

fruits_list = ["apple", "banana"]
fruits_list[0] = "cherry"
print(fruits_list)

fruits = ("apple", "banana", "cherry")

print(list(fruits))
print(tuple(fruits))

fruits[0] = "mango"

print(fruits)

person = ("john",)
print(type(person))

fruits = tuple(("apple", "cherry", "mango"))
print(fruits)
