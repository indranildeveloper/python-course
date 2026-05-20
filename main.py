"""
Milage Converter
"""

print("How many kms you have walked today?")
kms = input()

miles = float(kms) * 0.621371
miles = round(miles, 2)

print(f"You entered {kms} km which is equal to {miles} mile.")
