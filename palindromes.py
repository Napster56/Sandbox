"""
Program to check if a string is a palindrome; a string that reads the same
forward as backward
"""
import string

pal_1 = "Madam, I'm Adam"
pal_2 = "A man, a plan, a canal, Panama"
print("Forward: {} \nBackward: {}".format(pal_1, pal_1[:: -1]))
print("Forward: {} \nBackward: {}".format(pal_2, pal_2[:: -1]))



user_string = input("Enter a string")
modified_string = user_string.lower()

bad_chars = string.whitespace + string.punctuation

for char in modified_string:
    if char in bad_chars:  # remove bad characters
        modified_string = modified_string.replace(char, '')

if modified_string == modified_string[::-1]:
    print("The original string is: {}\n\
        the modified string is: {}\n\
        the reversal is : {}\n\
        String is a palindrome".format(user_string, modified_string, modified_string[::-1]))
else:
    print("The original string is: {}\n\
            the modified string is: {}\n\
            the reversal is : {}\n\
            String is not a palindrome".format(user_string, modified_string, modified_string[::-1]))