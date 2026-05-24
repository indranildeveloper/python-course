"""
Python break and continue keywords to control loop execution

The break keyword is used to break out a for loop, or a while loop.

The continue keyword is used to end the current iteration in a for loop (or a while loop), and continues to the next iteration.
"""

num = 1

while num < 11:
    print(num)
    if num == 5:
        break
    num += 1

for num in range(1, 11):
    if num > 5:
        break
    print(num)


for num in range(1, 11):
    if num == 5:
        continue
    print(num)

num = 0

while num < 10:
    num += 1
    if num == 5:
        continue
    print(num)
