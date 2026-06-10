"""
Python Inheritance

Inheritance allows us to define a class that inherits all the methods and properties from another class.

Parent class is the class being inherited from, also called base class.

Child class is the class that inherits from another class, also called derived class.

Create a Child Class
To create a class that inherits the functionality from another class, send the parent class as a parameter when creating the child class.
"""


class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def full_name(self):
        return f"The full name is: {self.first_name} {self.last_name}"


class Student(Person):
    def __init__(self, first_name, last_name, year):
        super().__init__(first_name, last_name)
        self.graduation_year = year

    def greet(self):
        return f"Welcome, {self.first_name} {self.last_name} to the class of {self.graduation_year}."


s_one = Student("John", "Doe", 2024)
print(s_one.graduation_year)
print(s_one.full_name())
print(s_one.greet())
