"""
Python OOP

What is OOP?

OOP stands for Object-Oriented Programming.

Python is an object-oriented language, allowing you to structure your code using classes and objects for better organization and reusability.

Advantages of OOP

- Provides a clear structure to programs
- Makes code easier to maintain, reuse, and debug
- Helps keep your code DRY (Don't Repeat Yourself)
- Allows you to build reusable applications with less code

What are Classes and Objects?
Classes and objects are the two core concepts in object-oriented programming.

A class defines what an object should look like, and an object is created based on that class. For example:

Class	Objects
Fruit	Apple, Banana, Mango
Car	    Volvo, Audi, Toyota

When you create an object from a class, it inherits all the variables and functions defined inside that class.

Python Classes and Objects

Python Classes/Objects
Python is an object oriented programming language.

Almost everything in Python is an object, with its properties and methods.

A Class is like an object constructor, or a "blueprint" for creating objects.
"""


class Person:
    name = "John"


person_one = Person()
person_two = Person()
person_three = Person()
person_four = Person()
person_five = Person()
# del person_one
print(person_one)
