# Program to reverse each line of the input files in the output file

input_file = open("input.txt", "r")
output_file = open("output.txt", "w")

for line in input_file:
    string = ""
    line = line.strip()  # remove carriage return
    for char in line:
        string = char + string          # concatenate at the left (reverse)
    print(string, file=output_file)     # print to output file

    # include a print to shell to view progress
    print("Line: {:12s} reversed is: {:s}".format(line, string))
input_file.close()
output_file.close()