"""
Ask user for their name
Tell them how many vowels are in their name
Tell them how many capitals are in their name
"""

count_vowels = 0
name = "Bobby McAardvark"
# name = input("Name: ")
for letter in name:
    if letter.lower() in 'aeiou':
        count_vowels += 1

print("Out of {} letters, {} has {} vowels".format(len(name), name, count_vowels))


# str function retuns a list of letters
print(str([letter for letter in name if letter.isupper()]))

# join is a string method & returns
print("".join([letter for letter in name if letter.isupper()]))