
import math

# floating point precision 3
value = "Value is {:.3f}".format(math.pi)
print(value)

name = "Monty"

money = 73.6

print("{} has ${:.2f}".format(name, money))

s = "CAT"
print(s.upper().lower(), type(s))


# string 10 spaces wide including argument, right justified
# decimal 4 spaces wide including argument, left justified
print("{:>10s} is {:<10d} years old.".format('Bill', 25))

# string 10 spaces wide including argument
# decimal 4 spaces wide including argument
for i in range(5):
    print("{:10d} --> {:4d}".format(i, i ** 2))


# To override the {}-to-argument matching using indices
print("{0} is {2} and {0} is also {1}".format("Bill", 25, "tall"))
