"""
Exception handling to demonstrate try / except /else / finally suites
"""


def process_file(data_file):
 # Program to print each line of a file with its line number
    count = 1
    for line in data_file:
        print(("line " + str(count)) + ": " + line.strip())
        count += 1

while True:     # Loop forever until 'break' is encountered
    filename = input("Enter a file to open: ")
    try:
        data_file = open(filename)
    except IOError:             # executes if file open fails
        print("Bad file name; try again")
    else:                    # executes if no exception and processes file
        print("Processing file", filename)
        process_file(data_file)
        break               # exits the while loop after executing the 'finally' block
    finally:                # executes whether there was an exception or not
        try:
            data_file.close()
        except NameError:
            print("Going again")


    print("Line after the try-except suite")



