"""
Python Polymorphism

The word "polymorphism" means "many forms", and in programming it refers to methods/functions/operators with the same name that can be executed on many objects or classes.

Function Polymorphism

An example of a Python function that can be used on different objects is the len() function.

Class Polymorphism

Polymorphism is often used in Class methods, where we can have multiple classes with the same method name.
"""


class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def move(self):
        print("Moving...")


class Car(Vehicle):
    pass


class Boat(Vehicle):
    def move(self):
        print("Sailing...")


class Plane(Vehicle):
    def move(self):
        print("Flying...")


car = Car("Ford", "Mustang")
boat = Boat("Boat Brand", "Boat Model")
plane = Plane("Boeing", "747")


for v in (car, boat, plane):
    print(v.brand)
    print(v.model)
    v.move()
