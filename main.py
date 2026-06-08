"""
Python Class Attributes

Class Properties

Properties are variables that belong to a class. They store data for each object created from the class.

Class Properties vs Object Properties

Properties defined inside __init__() belong to each object (instance properties).

Properties defined outside methods belong to the class itself (class properties) and are shared by all objects.
"""


class Person:
    species = "Human"
    person_created = 0

    def __init__(self, name, age=20):
        self.name = name
        self.age = age
        Person.person_created += 1

    def greet(self):
        return f"Hi there, {self.name}"

    def likes(self, thing):
        return f"{self.name} likes {thing}"

    def welcome(self):
        message = self.greet()
        print(message, "Welcome to our app.")


print(Person.person_created)
person_one = Person("John", 22)
person_two = Person("Jane", 24)
print(Person.person_created)


# print(Person.species)
