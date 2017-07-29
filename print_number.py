"""
Function that takes an integer and prints the numbers from that down to 0.
"""


# multiple carets = press CTRL twice, hold then up or down

# def print_down():
#     number = int(input("Enter a number:"))
#     for i in range(number + 1):
#         print(number)
#         number -= 1
#
# print_down()


# def print_down(start):
#     n = start
#     while n >= 0:
#         print(n)
#         n -= 1
#
# print_down(6)


# recursively
def print_down(n):
    print(n)
    if n > 0:
        return print_down(n - 1)

print_down(16)

