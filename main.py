"""
Python Lambda

Lambda Functions

A lambda function is a small anonymous function.
A lambda function can take any number of arguments, but can only have one expression.

Why Use Lambda Functions?

The power of lambda is better shown when you use them as an anonymous function inside another function.
Use lambda functions when an anonymous function is required for a short period of time.
"""

# def sum_ten(num):
#     return num + 10


# sum_ten = lambda num: num + 10

# sum_two_numbers = lambda a, b: a + b

# sum_three_numbers = lambda a, b, c: a + b + c

# print(sum_ten(5))
# print(sum_two_numbers(10, 15))
# print(sum_three_numbers(10, 20, 30))


def multiplier(factor):
    return lambda number: number * factor


double = multiplier(2)
triple = multiplier(3)

print(double(10))
print(triple(10))
