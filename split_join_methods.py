"""
Program to reverse the words in a string
Use: split & join - string methods

words = "This is a test"
string_elements = words.split()  # creates a list of words
print(string_elements)

reversed_elements = []
for element in string_elements:              # for each word
    reversed_elements.append(element[::-1])     # reverse & append to a new list
print(reversed_elements, type(reversed_elements))

new_str = ' '.join(reversed_elements)         # join with space separator

print(new_str)

words =list("This is a test")    # splits stringinto individual elements
words.reverse()
print(words)


# join method uses the calling string as the separator
strings = ["Hi", "Ho", "bye", "zap"]
new_str = ":".join(strings)   # calling string is colon :
print(new_str, type(new_str))
print(strings, type(strings))


