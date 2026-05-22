"""
Python Logical Operators

Combining Multiple Operators

You can combine multiple logical operators in a single expression. Python evaluates not first, then and, then or.
"""

age = 25
is_student = False
has_discount_code = True

if (age < 18 or age > 65) and not is_student or has_discount_code:
    print("Discount Applied!")
