"""
Exception handling for a program that reads a particular line from a file.
User enters the line number and the file name.
"""

file = input("Open what file: ")
find_line = input("Which line (integer)): ")

try:
    input_file = open(file)
    find_line = int(find_line)
    line_count = 1
    for line in input_file:
        if line_count == find_line:
            print("Line {} of file {} is {}".format(find_line, file, line))
            break
        line_count += 1
    else:
        print("Line {} of file {} not found.".format(find_line, file))
    input_file.close()
except IOError:
    print("The", file, "file doesn't exist.")
except ValueError:
    print("Line", find_line, "isn't a legal line number.")
