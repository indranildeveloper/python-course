"""
Python self Parameter

The self Parameter
The self parameter is a reference to the current instance of the class.

It is used to access properties and methods that belong to the class.

Why Use self?
Without self, Python would not know which object's properties you want to access.

self Does Not Have to Be Named "self":

It does not have to be named self, you can call it whatever you like, but it has to be the first parameter of any method in the class.

While you can use a different name, it is strongly recommended to use self as it is the convention in Python and makes your code more readable to others.
"""


class Person:
    def __init__(self, name, age=20):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hi there, {self.name}"

    def likes(self, thing):
        return f"{self.name} likes {thing}"

    def welcome(self):
        message = self.greet()
        print(message, "Welcome to our app.")


person_one = Person("John", 22)
person_two = Person("Jane", 24)

print(person_one.greet())
print(person_two.greet())

print(person_one.likes("Ice cream"))
print(person_two.likes("Candy"))

person_one.welcome()
person_two.welcome()
