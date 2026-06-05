"""
Python Modules

What is a Module?

Consider a module to be the same as a code library.
A file containing a set of functions you want to include in your application.
"""

# import random as rand
from random import randint as random_integer, choice

# from random import *

fruits = ["apple", "banana", "cherry"]

print(random_integer(1, 10))
print(choice(fruits))

# random.shuffle(fruits)

# print(fruits)
