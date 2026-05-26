"""
List Methods

Remove Specified Item

The remove() method removes the specified item.
If there are more than one item with the specified value, the remove() method removes the first occurrence.

Remove Specified Index

The pop() method removes the specified index.
If you do not specify the index, the pop() method removes the last item.

The del keyword also removes the specified index.
The del keyword can also delete the list completely.


Clear the List

The clear() method empties the list.
The list still remains, but it has no content.
"""

fruits = ["apple", "banana", "cherry", "orange", "banana"]
fruits.remove("banana")
removed_item = fruits.pop()
print(removed_item)

del fruits[1]
del fruits

fruits.clear()

print(fruits)
