"""
Python Dictionaries
"""

car_details = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964,
    "is_active": False,
    "colors": ["red", "black", "purple"],
}

print("abc" in car_details.keys())
print("Ford" in car_details.values())

if "model" in car_details:
    print("Yes, 'model' is one of the keys.")
