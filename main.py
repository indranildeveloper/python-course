"""
Python Functions

Default Parameter Values

You can assign default values to parameters. If the function is called without an argument, it uses the default value.
"""

# def greet(name="friend"):
#     print(f"Hello, {name}")


# greet()
# greet("John")

# my_list = [1, 2, 3]
# removed_value = my_list.pop()

# print(removed_value)


def add(num_one, num_two):
    return num_one + num_two


def subtract(num_one, num_two):
    return num_one - num_two


def math(num_one, num_two, fn=add):
    return fn(num_one, num_two)


print(math(2, 2))
print(math(10, 4, subtract))
