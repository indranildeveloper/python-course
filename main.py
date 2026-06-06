"""
Python __init__() Method

The __init__() Method
All classes have a built-in method called __init__(), which is always executed when the class is being initiated.

The __init__() method is used to assign values to object properties, or to perform operations that are necessary when the object is being created.
"""


class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age


person_one = Person("John", 22)
person_two = Person("Jane", 24)

print(person_one.name, person_one.age)
print(person_two.name, person_two.age)
