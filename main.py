"""
Python Class Methods

In Python, a class method is a method that is bound directly to the class rather than its individual object instances.
"""

from datetime import date


class Person:
    species = "Human"
    person_created = 0

    def __init__(self, name, age=20):
        self.name = name
        self.age = age
        Person.person_created += 1

    @classmethod
    def get_created_person_number(cls):
        return f"There are {Person.person_created} person created."

    @classmethod
    def from_birth_year(cls, name, year):
        age = date.today().year - year
        return cls(name, age)

    def greet(self):
        return f"Hi there, {self.name}"

    def likes(self, thing):
        return f"{self.name} likes {thing}"

    def welcome(self):
        message = self.greet()
        print(message, "Welcome to our app.")


person_one = Person("John", 22)
person_two = Person("Jane", 24)
person_three = Person.from_birth_year("Sara", 2000)
print(person_three.__dict__)
print(Person.get_created_person_number())
