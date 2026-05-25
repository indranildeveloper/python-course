"""
List Methods

Append Items
To add an item to the end of the list, use the append() method.

Insert Items
To insert a list item at a specified index, use the insert() method.
The insert() method inserts an item at the specified index.

Extend List
To append elements from another list to the current list, use the extend() method.
"""

fruits = ["apple", "banana", "cherry", "orange"]
# fruits.append("mango")
# second_fruit_list = ["mango", "kiwi"]
# fruits.extend(second_fruit_list)

fruits.insert(2, "mango")

print(fruits)
