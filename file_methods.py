"""
# readline method
temp = open("temp.txt", "r")   # open file for reading
first_line = temp.readline()   # reads exactly one line
print(first_line)

for line in temp:             # read remaining lines
    print(line)

temp.readline()               # read file, return empty string
print(temp)
temp.close()


# read method
temp = open("temp.txt", "r")   # open file for reading
print(temp.read(1))            # reads exactly one char

print(temp.read(2))            # reads next 2 chars

print(temp.read())             # read remaining file
temp.close()
"""

# readlines method
temp = open("temp.txt", "r")          # open file for reading
file_contents = temp.readlines()      # read all file lines into a list
print(file_contents)

string = "to be or not to be"
temp.write(string)
print(temp)
temp.close()


