"""
Python Type Annotations/Hints

Python type annotations (also known as type hints) are an optional syntax used to explicitly specify the expected data types of variables, function parameters, and return values.
"""

from typing import Union, Literal

name: str = "John"
age: int = 20

scores: list[int] = [10, 20, 30]
inventory: dict[str, int] = {"apples": 10, "bananas": 20}
coordinates: tuple[float, float, str] = (10.0, 20.0, "banana")


user_id: int | str = 10

theme: Literal["light", "dark"] = "light"


def greet(name: str) -> str:
    return f"Hello, {name.upper()}"


result = greet("John")
