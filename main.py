"""
Python Closure

In Python, a closure is a nested function object that retains access to variables from its enclosing outer scope, even after the parent function has finished executing. It essentially bundles a function together with an environment or data "attached" to it.

Criteria for a Closure
A closure is formed in Python when three conditions are met:

- There must be a nested function (a function inside a function).
- The inner function must reference a variable from the outer function's scope (a "free variable").
- The outer function must return the inner function object.
"""

# def make_multiplier(factor):
#     def multiply(number):
#         return number * factor

#     return multiply


# double = make_multiplier(2)
# triple = make_multiplier(3)

# print(double(5))
# print(triple(5))


def make_counter():
    count = 0

    def counter():
        nonlocal count
        count += 1
        return count

    return counter


my_counter = make_counter()
print(my_counter())
print(my_counter())
