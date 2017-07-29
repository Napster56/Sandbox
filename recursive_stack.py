"""
Function uses print statements to show how the stack operation in factorial
recursion.
"""


def fact(n):
    print("n", n)
    if n < 2:          # base case
        return 1
    else:
        result = n * fact(n - 1)       # recursive step
        print("Result = ", result)
        return result

fact(12)