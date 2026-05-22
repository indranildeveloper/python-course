"""
Python Logical Operators

Logical operators are used to combine conditional statements. Python has three logical operators:

    and - Returns True if both statements are true
    or - Returns True if one of the statements is true
    not - Reverses the result, returns False if the result is true
"""

a = 200
b = 40
c = 500

if a > b and c > a:
    print("Conditions are true.")

if a > b or a > c:
    print("Here at least one condition is true.")
