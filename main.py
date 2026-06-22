"""
Python File Write

Write to an Existing File

To write to an existing file, you must add a parameter to the open() function:

- "a" - Append - will append to the end of the file
- "w" - Write - will overwrite any existing content
"""

with open("demo.txt", "a") as text_file:
    # text_file.write("Hello World.\n")
    # text_file.write("Hello World again.\n")
    # text_file.write("This is a new line.\n")
    text_file.write("Hi there.")
