s = "Hello World"

print(s[0], s[-1], s[1:5], s[:-3])

print(len(s))

print(s[0] == "H")

# slicing

print(s[1:5], s[:-3], s[3:], s[:])

# slicing takes 3 args [star:finish:step]

print(s[3:10:2], s[::2])

# compare first two characters of a string

print(s[:2])


# print each character individually

for c in s:
    print(c)

for c in s[:7]:
    print(c, type(c))

# type convert int into string to concatenate

total = "s" + str(1)
print(total)

# find operator
print(s.find("W"))

# membership operator 'in'

print("H" in s)
# True

print("ell" in s)
# True

print("h" in s)
# False

# Python is strongly typed language; won't try and add str + int

sum = "s" + 1
print(sum)

"""
sum = "s" + 1
TypeError: Can't convert 'int' object to str implicitly
"""

s



print(s[20])    # string index out of range

"""
Traceback (most recent call last):
  File "F:/CP1404 Programming I/Sandbox/strings.py", line 7, in <module>
    print(s[20])
IndexError: string index out of range
"""


