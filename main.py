"""
Python raise Keyword

The raise keyword is used to raise an exception.
You can define what kind of error to raise, and the text to print to the user.
"""

# positive_number = -1

# if positive_number < 0:
#     raise Exception("Hey you can not provide and number less than zero.")
# else:
#     print("Your number is all good!")

number = "hello"

if not type(number) is int:
    raise TypeError("Only integers are allowed.")
else:
    print("Your number is all good!")
