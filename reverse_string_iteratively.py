"""
Functions to reverse a string iteratively.

"""

my_string = "aeiouabcdefghi"


# using extended slice syntax
reverse_string = my_string[:: -1]
print(reverse_string)


# using a for loop
def reverse(text):
    # code goes here
    result = ''
    for i in range(len(text) - 1, -1, -1):
        result += text[i]
    return result


# keep this function call here
# to see how to enter arguments in Python scroll down
print(reverse(my_string))

