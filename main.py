"""
Set comprehension

Set comprehension is a concise way to create sets in Python by iterating over an iterable (like a list, string, or range) and applying an optional condition.

The basic syntax for a set comprehension is:
{expression for item in iterable if condition}
"""

num_set = {num for num in [1, 2, 2, 2, 3]}
square_set = {num**2 for num in range(1, 11)}
even_nums = {num for num in range(1, 11) if num % 2 == 0}
str_set = {char.upper() for char in "hello"}
# print(num_set)
# print(square_set)
# print(even_nums)
print(str_set)
