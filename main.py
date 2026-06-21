"""
Python Generators

Generators are iterators.

Generators are functions that can pause and resume their execution.

When a generator function is called, it returns a generator object, which is an iterator.

The code inside the function is not executed yet, it is only compiled. The function only executes when you iterate over the generator.

Generators allow you to iterate over data without storing the entire dataset in memory.

Instead of using return, generators use the yield keyword.

The yield Keyword

The yield keyword is what makes a function a generator.

When yield is encountered, the function's state is saved, and the value is returned. The next time the generator is called, it continues from where it left off.
"""

# def count_up_to(num):
#     count = 1
#     while count <= num:
#         yield count
#         count += 1


# print(count_up_to(5))
# for num in count_up_to(5):
#     print(num)


# def generate_person():
#     yield "John"
#     yield "Jane"
#     yield "Sara"


# person_generator = generate_person()

# print(next(person_generator))
# print(next(person_generator))
# print(next(person_generator))
# print(next(person_generator))


def large_sequence(number):
    for num in range(number):
        yield num
        # print(num)


# sequence_generator = large_sequence(1000000)

# large_sequence(10000000000)

for num in large_sequence(1000000):
    print(num)

# print(next(sequence_generator))
# print(next(sequence_generator))
# print(next(sequence_generator))
# print(next(sequence_generator))
# print(next(sequence_generator))
