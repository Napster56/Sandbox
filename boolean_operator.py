
numerator = int(input("Enter a numerator: "))
denominator = int(input("Enter a denominator: "))

"""
Without Boolean operator:

print(numerator / denominator)
Enter a numerator: 12
Enter a denominator: 0
Traceback (most recent call last):
  File "G:/CP1404 Programming I/Sandbox/boolean_operator.py", line 4, in <module>
    print("Okay")
ZeroDivisionError: division by zero
"""


if denominator != 0 and numerator % denominator == 0:
    print("Okay")
else:
    print("Error")
