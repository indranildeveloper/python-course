"""
Python *args and **kwargs

*args and **kwargs

By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.

Arbitrary Arguments - *args

If you do not know how many arguments will be passed into your function, add a * before the parameter name.
This way, the function will receive a tuple of arguments and can access the items accordingly.
Arbitrary Arguments are often shortened to *args in Python documentation.

What is *args?

The *args parameter allows a function to accept any number of positional arguments.
Inside the function, args becomes a tuple containing all the passed arguments.
"""


def sum_numbers(*numbers):
    print(numbers)
    total = 0
    for num in numbers:
        total += num
    return total


print(sum_numbers(1, 2, 3, 4, 5))
print(sum_numbers(10, 20))
print(sum_numbers(5))
