"""
Multiple Inheritance

Multiple inheritance in Python is a feature that allows a child class to inherit attributes and methods from more than one parent class.
"""


class Flyer:
    def __init__(self, name):
        self.name = name

    def fly(self):
        return f"{self.name} flying high in the sky."

    def greet(self):
        return f"Hello from flyer {self.name}"


class Swimmer:
    def __init__(self, name):
        self.name = name

    def swim(self):
        return f"{self.name} is swimming good in the pond."

    def greet(self):
        return f"Hello from swimmer {self.name}"


class Duck(Flyer, Swimmer):
    def __init__(self, name):
        super().__init__(name)


captain_cook = Duck("Captain Cook")
print(captain_cook.fly())
print(captain_cook.swim())
print(captain_cook.greet())
