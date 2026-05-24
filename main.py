"""
Python enumerate() Function

The enumerate() function takes a collection (e.g. a tuple, a string) and returns it as an enumerate object.

The enumerate() function adds a counter as the key of the enumerate object.
"""

message = "hello"
# print(list(enumerate(message)))

for index, character in enumerate(message):
    print(f"The character at the index {index} is {character}")
