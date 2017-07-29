"""
Function to add up numbers from 0 to n.
"""


def add_numbers(n):
    if n == 0:
        return 0
    return n + add_numbers(n - 1)

print(add_numbers(5))


def recurse(n):
    if n <= 0:
        print("Done")
    else:
        print(n)
        recurse(n - 1)
        print(n)

recurse(6)