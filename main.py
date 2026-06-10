"""
Python Encapsulation
"""


class Person:
    def __init__(self, name, age, salary):
        self.name = name
        self.__age = age  # private property
        self._salary = salary  # protected property

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, new_age):
        if self.__validate_age(new_age):
            self.__age = new_age

    # def get_age(self):
    #     return self.__age

    def __validate_age(self, age):
        if age > 0:
            return True
        else:
            raise ValueError("Age can not be less than zero.")

    # def set_age(self, new_age):
    #     if self.__validate_age(new_age):
    #         self.__age = new_age


person_one = Person("John", 24, 50000)

# person_one.set_age(30)
# print(person_one.get_age())

person_one.age = 30
print(person_one.age)
