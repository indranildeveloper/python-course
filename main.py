"""
Python Functions

Python Function Arguments

Arguments

Information can be passed into functions as arguments.

Arguments are specified after the function name, inside the parentheses. You can add as many arguments as you want, just separate them with a comma.

Parameters vs Arguments

The terms parameter and argument can be used for the same thing: information that are passed into a function.

From a function's perspective:
A parameter is the variable listed inside the parentheses in the function definition.
An argument is the actual value that is sent to the function when it is called.

Number of Arguments

By default, a function must be called with the correct number of arguments.
"""


def greet(name):  # name -> parameter
    print(f"Hi there, {name}")


# greet("John")  # "John" -> argument
# greet("Jane")
# greet("Sara")


def sum_nums(num_one, num_two):
    return num_one + num_two


result = sum_nums(5, 8)
print(result)
