"""
Function that calculates the factorial of n and prints the result.

"""


def main():
    n = factorial(1)
    print(n)                 # print result for first function
#   n = factorial_2(0)
#   print(n)                 # prints result for second function


def factorial(n):
    """ Recursive factorial. """
    if n == 1 or n == 0:                # n >= 0, factorial of a negative number is undefined
        return 1                        # base case
    # else:  redundant because return stops the function
    return n * factorial(n - 1)     # recursive case


# as a for loop
# def factorial_2(n):
#     for i in range(n):
#         if n == 1 or n == 0:
#             return 1
#         return n * (n - 1)

main()
