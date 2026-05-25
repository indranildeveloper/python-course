"""
Python Lists

Lists are used to store multiple items in a single variable.

In other programming languages we have the similar data structure which is Array.

Lists are ordered

When we say that lists are ordered, it means that the items have a defined order, and that order will not change.

If you add new items to a list, the new items will be placed at the end of the list.
"""

fruit_one = "apple"
fruit_two = "orange"
fruit_three = "banana"

fruits_list = [fruit_one, fruit_two, fruit_three]
my_list = ["abc", True, True, False, 5, 6.4]

print(len(fruits_list))
print(type(my_list))

r = range(10)
print(list(r))

fruits_list = list(("apple", "banana", "cherry"))
print(fruits_list)
