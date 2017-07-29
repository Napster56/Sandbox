"""
Function to sum a list recursively.
"""

numbers = [1, 2, 3, 4, 5]


def sum_list(numbers):
    if len(numbers) == 1:          # base case is always an if statement
        return numbers[0]
    return numbers[0] + sum_list(numbers[1:])    # must contain the function


print(sum_list(numbers))

result = sum(numbers)
print("The sum of {} is {}".format(numbers, result))

"""
def sum_list_iteratively(numbers):
    # iterative version
    total = 0
    for number in numbers:
        total += number
        # print(total)        # prints on each iteration
    return total            # only prints at end

print(sum_list_iteratively(numbers))
"""
