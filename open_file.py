"""
Function that takes in a filename and returns the longest line
of the file(line number, length
"""

def get_longest_line(filename):
    """open filename for reading as file
        line_number, length = ??
        close file
        return (line_number, length) as tuple
    """

    # input_file = open(filename, 'r')
    with open(filename, 'r') as input_file:  # opens file as read and closes file
        lines = input_file.readlines()       #
        lengths = [len(line.strip()) for line in lines]
        max_length = max(lengths)
        longest_line = lengths.index(max_length)
    # input_file.close()
    return longest_line + 1, max_length

print(get_longest_line("guitar.txt"))