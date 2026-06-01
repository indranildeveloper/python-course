"""
Python *args and **kwargs

*args and **kwargs

By default, a function must be called with the correct number of arguments.
However, sometimes you may not know how many arguments that will be passed into your function.

*args and **kwargs allow functions to accept a unknown number of arguments.

Arbitrary Keyword Arguments - **kwargs

If you do not know how many keyword arguments will be passed into your function, add two asterisks ** before the parameter name.
This way, the function will receive a dictionary of arguments and can access the items accordingly.
Arbitrary Keyword Arguments are often shortened to **kwargs in Python documentation.

Using **kwargs with Regular Arguments

You can combine regular parameters with **kwargs.

Combining *args and **kwargs

You can use both *args and **kwargs in the same function.
"""


def greet(username, *args, **kwargs):
    print(args)
    print(kwargs)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    age = kwargs["age"]
    print(f"Hello there: {first_name} {last_name}, you are {age}")
    print(f"Your username is {username}")


greet("john", 40, "hi there", first_name="John", last_name="Doe", age=25, country="USA")
