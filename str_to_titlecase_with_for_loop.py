"""
program to convert a string to titlecase using a for loop
"""


number = "074295079"
if number.startswith("07"):
    print(True)
elif number.isdecimal()


my_string = "hello world"
# my_string = my_string.title()

# my_string = "hello world".title()
# print(my_string)

string_elements = my_string.split()  # convert string to a list
title_words = []
for word in string_elements:
    word = word.title()
    title_words.append(word)  # create a new list

my_string = ' '.join(title_words) # convert list back to a string
print(my_string)





