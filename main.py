"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator.
"""

fruits = ["apple", "banana", "cherry"]
fruits_iterator = iter(fruits)

for fruit in fruits:
    print(fruit)

print(next(fruits_iterator))
print(next(fruits_iterator))
print(next(fruits_iterator))
# print(next(fruits_iterator))

favorite_fruit = "apple"
favorite_fruit_iterator = iter(favorite_fruit)

print(next(favorite_fruit_iterator))
print(next(favorite_fruit_iterator))
print(next(favorite_fruit_iterator))
print(next(favorite_fruit_iterator))
print(next(favorite_fruit_iterator))
