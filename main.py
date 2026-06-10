"""
Method Resolution Order (MRO)

When multiple parent classes share a method with the same name, Python needs a way to decide which one to execute. Python uses the C3 Linearization algorithm to build the Method Resolution Order (MRO).

How we can check for MRO:
1. __mro__
2. mro()
3. help()
"""


class A:
    def greet(self):
        print("Hello from A.")


class B(A):
    def greet(self):
        print("Hello from B.")


class C(A):
    def greet(self):
        print("Hello from C.")


class D(B, C):
    def __init__(self):
        super().__init__()

    def greet(self):
        print("Hello from D.")


my_obj = D()
my_obj.greet()
# print(D.__mro__)
# print(D.mro())
# print(help(D))
