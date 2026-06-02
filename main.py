"""
Python filter() Function

The filter() function returns an iterator where the items are filtered through a function to test if the item is accepted or not.
"""

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))

print(even_numbers)

ages = [5, 10, 20, 7, 8, 18, 64, 32]


def filter_adults(age):
    if age < 18:
        return False
    else:
        return True


adults = list(filter(filter_adults, ages))

print(adults)
