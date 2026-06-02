"""
Python sorted() Function

The sorted() function returns a sorted list of the specified iterable object.

You can specify ascending or descending order. Strings are sorted alphabetically, and numbers are sorted numerically.

Note: You cannot sort a list that contains BOTH string values AND numeric values.
"""

# alphabets = ("b", "g", "z", "d", "x", "u", "j", "h")

# sorted_alphabets = sorted(alphabets)

# print(sorted_alphabets)

nums = [1, 11, 45, 2, 6, 75, 9]
alphabets = ("b", "g", "z", "d", "x", "u", "j", "h")
people = ["John", "Jane", "Mary", "Sally"]


def get_closest(num):
    return abs(10 - num)


sorted_numbers = sorted(nums, key=get_closest)
sorted_alphabets = sorted(alphabets, reverse=True)
sorted_people = sorted(people, key=len, reverse=True)

print(sorted_numbers)
# print(sorted_alphabets)
# print(sorted_people)
