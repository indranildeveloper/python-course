"""
List Methods

Python List index() Method
The index() method returns the position at the first occurrence of the specified value.

Python List count() Method
The count() method returns the number of elements with the specified value.

Python List reverse() Method
The reverse() method reverses the sorting order of the elements.

Python List sort() Method
The sort() method sorts the list ascending by default.

Python String join() Method
The join() method takes all items in an iterable and joins them into one string.
"""

fruits = ["apple", "banana", "cherry", "kiwi", "mango", "orange", "cherry"]

print(fruits.index("apple"))
print(fruits.count("cherry"))

fruits.reverse()
fruits.sort(reverse=False)
print(fruits)

fruits_str = "#".join(fruits)
print(fruits_str)
