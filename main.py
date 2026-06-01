"""
Unpacking Arguments
"""


def sum_numbers(a, b, c):
    return a + b + c


numbers = (1, 2, 3)

print(sum_numbers(*numbers))  # sum_numbers(1, 2, 3)
