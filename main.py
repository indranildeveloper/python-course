"""
Python String Formatting

F-String was introduced in Python 3.6, and is now the preferred way of formatting strings.
Before Python 3.6 we had to use the format() method.
"""

price = 20
tax = 0.25
# msg = "The price is " + str(price) + " dollars"
msg = f"The total price is {(price + (price * tax)):.2f} dollars"
print(msg)
