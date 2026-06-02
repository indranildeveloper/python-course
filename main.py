"""
Python map() Function

The map() function executes a specified function for each item in an iterable. The item is sent to the function as a parameter.
"""

# def my_function(item):
#     return len(item)


fruits_one = ("apple", "banana", "cherry")
fruits_two = ("orange", "lemon", "pineapple")

fruit_lengths = list(
    map(lambda item_one, item_two: item_one + item_two, fruits_one, fruits_two)
)

print(fruit_lengths)
