import random

numbers = [10, 20, 30, 40, 50, 100]
random.shuffle(numbers)               # shuffles number in list
print(numbers)

for number in sorted(numbers):        # sorted function: sorts number in list,
    print(number, end=' ')            # but does not modify the list

print(numbers)

print(numbers.sort())                 # returns none

print(numbers)