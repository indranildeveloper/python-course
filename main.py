"""
Truthy and Falsy Values

In Python, every object has an inherent "truthiness" value when evaluated in a boolean context, such as an if statement or a while loop. While there are specific "falsy" values that resolve to False, almost everything else in Python is considered "truthy" and resolves to True.

Falsy Values

Values are considered falsy if they represent "nothing" or are explicitly defined as false. The standard falsy values in Python include:

- Constants: None and False.

- Numeric Zeroes: 0 (integer), 0.0 (float), 0j (complex), and other numeric variations of zero.

- Empty Sequences and Collections:

- Empty string: "" or ''.
- Empty list: [].
- Empty tuple: ().
- Empty dictionary: {}.
- Empty set: set().

- Custom Objects: Any object where the class defines a __bool__() method that returns False or a __len__() method that returns 0

Truthy Values

Values are considered truthy if they are not falsy. Common examples include:

- Non-zero numbers: Any positive or negative number like 1, -42, or 3.14.

- Non-empty strings: Even a string with just a space " " is truthy.

- Non-empty collections: Any list, tuple, or dictionary that contains at least one item, such as [0], {"key": "value"}, or (False,).

- Functions and Classes: All functions and user-defined class instances (unless specifically overridden) are truthy.
"""

# num = 0

# if num:
#     print(f"Your number is {num}")
# else:
#     print("Your number represents false.")

# print(bool(0))
# print(bool(5))
# print(bool("hello"))
# print(bool(""))

num = input("Hey, enter a number: ")

if num:
    print(f"You entered the number: {num}")
else:
    print("Hey, you did not enter a number.")
