"""
Demo infinite loop using while True
"""

while True:
    for x in range(6):
        y = 2 * x + 1
        print(y, end='')
        if y > 9:
            break

