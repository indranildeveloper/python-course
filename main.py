"""
Python Try Except

The try block lets you test a block of code for errors.

The except block lets you handle the error.

The else block lets you execute code when there is no error.

The finally block lets you execute code, regardless of the result of the try- and except blocks.
"""

try:
    # print(fruits)
    names = []
    names[5]
    print("hello")
except NameError as error:
    print("Name Error Occurred.")
    print(error)
    raise NameError("do something else.")
except:
    print("Something went wrong.")
else:
    print("Nothing went wrong.")
finally:
    print("The try and except block finished.")
