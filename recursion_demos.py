"""
Function that takes an integer and prints the numbers
from that down to 0 using recursion.
"""

# use debugger to view the stack operation in recurse fn.
def recurse(n):
    if n <= 0:       # base case
        print("Done")
    else:
        print(n)
        recurse(n - 1)
        print(n)

recurse(4)

