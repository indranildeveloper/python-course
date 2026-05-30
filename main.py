"""
Python Functions

Return Values

Functions can send data back to the code that called them using the return statement.
When a function reaches a return statement, it stops executing and sends the result back.
If a function doesn't have a return statement, it returns None by default.

The pass Statement

Function definitions cannot be empty. If you need to create a function placeholder without any code, use the pass statement.
The pass statement is often used when developing, allowing you to define the structure first and implement details later.
"""

# nums = [1, 2, 3, 4, 5]

# print(len(nums))


def get_greeting():
    print("Before return.")
    return "Hello There!"
    print("After return.")


# message = get_greeting()

# print(get_greeting())


def my_function():
    pass
