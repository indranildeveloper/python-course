"""
Python Set Methods

Add Items

Once a set is created, you cannot change its items, but you can add new items.
To add one item to a set use the add() method.

Remove Item

To remove an item in a set, use the remove(), or the discard() method.
If the item to remove does not exist, remove() will raise an error.
If the item to remove does not exist, discard() will NOT raise an error.

You can also use the pop() method to remove an item, but this method will remove a random item, so you cannot be sure what item that gets removed.
Sets are unordered, so when using the pop() method, you do not know which item that gets removed.

The clear() method empties the set.

The del keyword will delete the set completely.

Copy a set

We can use the copy() method to copy a set.

Set Math:

Set union() Method
Return a set that contains all items from both sets, duplicates are excluded.

Set intersection() Method
Return a set that contains the items that exist in both set x, and set y.
"""

fruits_set = {"apple", "orange", "banana", "cherry"}
new_fruit_set = {"pineapple", "melon"}
# fruits_set.add("mango")
fruits_set.update(new_fruit_set)

# fruits_set.remove("banana")
# fruits_set.discard("abc")
# removed_item = fruits_set.pop()
# print(removed_item)

# fruits_set.clear()
# del fruits_set

# fruits_copy = fruits_set.copy()
# print(fruits_copy is fruits_set)

x = {"apple", "banana", "cherry"}
y = {"google", "microsoft", "apple"}

# z = x.union(y)
z = x.intersection(y)
print(z)
