"""
Python is vs ==

In Python, the primary difference is that == compares values, while is compares identities (memory locations).
"""

a = [1, 2]
b = [1, 2]

print(a == b)
print(a is b)
