"""
Strings are immutable
"""

word = "spam"
# word[1] = "l"
# print(word)

"""
Traceback (most recent call last):
  File "F:/CP1404 Programming I/Sandbox/slicing.py", line 2, in <module>
    word[1] = "l"
TypeError: 'str' object does not support item assignment
"""

new_word = word[:1] + 'l' + word[2:]  # create a new string using concatenation
print(new_word)                       # no spaces between letters

print(new_word.isupper(), new_word.isnumeric(), new_word.islower())