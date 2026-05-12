"""
Strings in Python

In Python, a string is an immutable sequence of Unicode characters used to represent text data. Because they are immutable, any operation that seems to "change" a string actually creates a brand new string object in memory.

Strings in python are surrounded by either single quotation marks, or double quotation marks.

'hello world' is the same as "hello world".
"""

my_name = "Indra"
msg = "he said, 'hi there'"

multiline_message = """This
is 
a
multiline 
string!
"""

print(msg)
print(my_name)
print(multiline_message)
print(type(my_name))
