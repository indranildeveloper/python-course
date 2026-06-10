"""
Python Encapsulation

Encapsulation is about protecting data inside a class.

It means keeping data (properties) and methods together in a class, while controlling how the data can be accessed from outside the class.

This prevents accidental changes to your data and hides the internal details of how your class works.

Why Use Encapsulation?

Encapsulation provides several benefits:

- Data Protection: Prevents accidental modification of data
- Validation: You can validate data before setting it
- Flexibility: Internal implementation can change without affecting external code
- Control: You have full control over how data is accessed and modified
"""


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.__age = age  # private property
        self._salary = salary  # protected property

    def get_age(self):
        return self.__age

    def __validate_age(self, age):
        if age > 0:
            return True
        else:
            raise ValueError("Age can not be less than zero.")

    def set_age(self, new_age):
        if self.__validate_age(new_age):
            self.__age = new_age


person_one = Person("John", 24, 50000)
# person_one.age = 30

print(person_one.age)
