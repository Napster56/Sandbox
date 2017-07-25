"""
Program to count the letters in string;
ignore characters that are not letters
"""

import string

user_string = input("Enter a string: ")


def count_letters(user_string):
    count = 0
    for char in user_string:
        if char.lower() in string.ascii_lowercase:
            count += 1

    print("There are {} letters in your string".format(count))

count_letters(user_string)
