"""
Function that returns the median value from from a list of numbers
"""

numbers = [34, 5, 45, 78, 89, 36, 56, 68, 99, 104, 12, 17]
# numbers = [1, 2, 3, 4, 5]


def get_median():
    numbers.sort()
    print(numbers)
    n = len(numbers)

    if not n % 2:
        #  floor division // returns an integer
        return sum(numbers[n // 2 - 1:n // 2 + 1]) / 2.0
    return numbers[n // 2]    # list index must be an integer


pprint(get_median())




