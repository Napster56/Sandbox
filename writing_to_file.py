# open file for writing
# creates file if it does not exist
# overwrites file if it exists


"""
temp_file = open("temp.txt", "w")                       # function

print("first line", file=temp_file)
print("second line", file=temp_file)

temp_file.close()  # method
"""

"""
temp_file = open("temp.txt", "a")                       # function

print("third line", file=temp_file)

temp_file.close()  # method
"""

"""
temp_file = open("temp.txt", "r+")                       # function
print("last line", file=temp_file)
temp_file.close()  # method
"""

# read & write - clears file contents
temp_file = open("temp.txt", "w+")                       # function

temp_file.close()  # method