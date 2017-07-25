"""
Function that asks user for a number and returns the number squared
"""


def main():

    number = int(input("Enter a number: "))

    def square(num):
        return num ** 2

    print(number, '^ 2 = ', square(number))

main()
