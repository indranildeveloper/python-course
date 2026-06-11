"""
Python staticmethod

In Python, @staticmethod is a decorator used to define a method inside a class that does not access or modify the class state or instance state. It behaves exactly like a regular function but lives within the class's namespace for logical grouping.
"""


class MathOperations:
    description = "A simple math utility."

    @staticmethod
    def add(num_one, num_two):
        return num_one + num_two

    @staticmethod
    def is_even(num):
        return num % 2 == 0


sum_result = MathOperations.add(5, 10)
is_even_result = MathOperations.is_even(5)
print(sum_result)
print(is_even_result)
