"""
Python parameter ordering in functions

- parameters
- *args
- default parameters
- **kwargs
"""


def greet(username, *args, person_name="John Doe", **kwargs):
    print(username)
    print(args)
    print(kwargs)
    print(person_name)
    first_name = kwargs["first_name"]
    last_name = kwargs["last_name"]
    age = kwargs["age"]
    print(f"Hello there: {first_name} {last_name}, you are {age}")
    print(f"Your username is {username}")


greet("john", 40, "hi there", first_name="John", last_name="Doe", age=25, country="USA")
