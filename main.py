"""
Python Dictionaries

Dictionary Comprehension in Python

Dictionary comprehension is a concise way to create dictionaries in Python using a single line of code.

Syntax:
<dict_name> = {<new_key>:<new_value> for <item> in <iterable>}
"""

squares = {num: num**2 for num in range(1, 11)}
# print(squares)

person = {" Name": "John", " CITY ": "London"}
cleaned_data = {key.strip().lower(): value.upper() for key, value in person.items()}

# print(cleaned_data)

ratings = {"John": 4.7, "Jane": 3.9, "Sara": 4.2}
top_rated = {name: score for name, score in ratings.items() if score >= 4.0}

# print(top_rated)

scores = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
results = {score: "pass" if score >= 50 else "retry" for score in scores}

print(results)
