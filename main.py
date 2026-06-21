"""
Python Generators

Generator Expressions

Similar to list comprehensions, you can create generators using generator expressions with parentheses instead of square brackets.
"""

# def square_numbers():
#     for num in range(5):
#         yield num * num


# square_numbers_generator = square_numbers()

# square_numbers_generator = (num * num for num in range(5))

# print(square_numbers_generator)

# for num in square_numbers_generator:
#     print(num)


# def echo_generator():
#     while True:
#         received = yield
#         print("Received: ", received)


# generator = echo_generator()
# next(generator)

# generator.send("Hello")
# generator.send("World")


def my_generator():
    try:
        yield 1
        yield 2
        yield 3
    finally:
        print("Generator closed.")


generator = my_generator()
print(next(generator))
print(next(generator))
generator.close()
