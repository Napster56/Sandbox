"""
Function to reverse a string recursively.

"""


def reverse_string(my_string):
    """ Recursive function to reverse a string """
    print("First invocation: ", my_string)
    # base case
    if len(my_string) == 1:
        print("base case")
        return my_string
    # recursive step
    else:
        modified_string = reverse_string(my_string[1:]) + my_string[0]
        print( "Reassembling {} and {} into {}".format(my_string[1:], my_string[0], modified_string))
        return modified_string

my_string = input("Reverse what string: ")
print()
result = reverse_string(my_string)
print("The reverse of {} is {}".format(my_string, result))

