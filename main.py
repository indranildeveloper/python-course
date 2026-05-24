"""
Python Match

The match statement is used to perform different actions based on different conditions.

The Python Match Statement

Instead of writing many if..else statements, you can use the match statement.

The match statement selects one of many code blocks to be executed.
"""

day = 6

match day:
    case 1:
        print("Sunday")
    case 2:
        print("Monday")
    case 3:
        print("Tuesday")
    case 4:
        print("Wednesday")
    case 5:
        print("Thursday")
    case 6:
        print("Friday")
    case 7:
        print("Saturday")
    # Default case
    case _:
        print("Hey, this is not a valid day.")

match day:
    case 2 | 3 | 4 | 5:
        print("This is a week day.")
    case 1 | 6 | 7:
        print("Hey, I love weekends!")
