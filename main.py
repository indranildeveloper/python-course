"""
Python min() Function

The min() function returns the item with the lowest value, or the item with the lowest value in an iterable.
If the values are strings, an alphabetically comparison is done.

Python max() Function

The max() function returns the item with the highest value, or the item with the highest value in an iterable.
If the values are strings, an alphabetically comparison is done.
"""

lowest = min(10, 5, 23, 8)
highest = max(10, 5, 23, 8)

numbers = [45, 23, 99, 65, 78, 4]

names = ["Alice", "Bob", "Charlie", "David"]

empty_list = []

prices = {"apple": 1.5, "banana": 0.8, "cherry": 3.0}

print(min(prices.values()))
print(max(prices.values()))

print(max(prices, key=prices.get))

# print(min(empty_list, default="Hey, there is no item."))

# print(min(names, key=lambda n: len(n)))
# print(max(names, key=lambda n: len(n)))
# print(min(names, key=len))
# print(max(names, key=len))

# print(lowest)
# print(highest)
# print(min(numbers))
# print(max(numbers))

# print(min("banana", "apple", "cherry"))
# print(max("banana", "apple", "cherry"))
