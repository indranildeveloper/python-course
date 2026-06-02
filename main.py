"""
Python all() Function

The all() function returns True if all items in an iterable are true, otherwise it returns False.
If the iterable object is empty, the all() function also returns True.
When used on a dictionary, the all() function checks if all the keys are true, not the values.

Python any() Function

The any() function returns True if any item in an iterable are true, otherwise it returns False.
If the iterable object is empty, the any() function will return False.
When used on a dictionary, the any() function checks if any of the keys are true, not the values.
"""

my_list = [True, True, True]
my_tuple = (0, 1, 1)
my_set = {0, 1, 0}
my_dictionary = {0: "apple", 1: "banana"}

# result = all(my_dictionary)
result = any(my_dictionary)

print(result)
