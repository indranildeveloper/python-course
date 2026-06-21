"""
Python Iterators
An iterator is an object that contains a countable number of values.

An iterator is an object that can be iterated upon, meaning that you can traverse through all the values.

Technically, in Python, an iterator is an object which implements the iterator protocol, which consist of the methods __iter__() and __next__().

Iterator vs Iterable

Lists, tuples, dictionaries, and sets are all iterable objects. They are iterable containers which you can get an iterator from.

All these objects have a iter() method which is used to get an iterator.

The string "HELLO" is an iterable, but it is not an iterator.

iter("HELLO") returns an iterator.
"""


class Counter:
    def __init__(self, number, upper_limit):
        self.number = number
        self.upper_limit = upper_limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.number <= self.upper_limit:
            next_number = self.number
            self.number += 1
            return next_number
        else:
            raise StopIteration


counter = Counter(1, 50)
counter_iterator = iter(counter)

for num in counter_iterator:
    print(num)
