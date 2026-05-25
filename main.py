"""
Iterating over lists
"""

fruits = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]

for fruit in fruits:
    print(fruit)

for idx in range(len(fruits)):
    print(fruits[idx])

idx = 0

while idx < len(fruits):
    print(f"{idx}: {fruits[idx]}")
    idx += 1

for idx, fruit in enumerate(fruits):
    print(f"{idx}: {fruit}")
