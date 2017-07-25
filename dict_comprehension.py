"""
Dictionary comprehension to create a dict from a string
"""

letters = {k: letter for k, letter in enumerate('abcdefgh')}
print(letters)

# reverse key-value pairs
letters_reversed = {letter: k for k, letter in letters.items()}
print(letters_reversed)

# sorted function only sorts the keys
print(sorted(letters_reversed))

# create a list then sort
letters2 = [(letter, k) for k, letter in letters_reversed.items()]
print(letters2)
sorted(letters2)
print(letters2, type(letters2))
