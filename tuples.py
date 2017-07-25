# multiple assignment

a, b = 2, 3
print(a, type(a))
print(b, type(b))

# create a tuple by using a comma

c = 2, 3
print(c, type(c))     # ( is tuple

a, b = (1, 2)       # (1, 2) is tuple
print(a, type(a))   # 1 <class 'int'>


# string can be split() into a list, and the results stored in a tuple
date_input = input("Enter DOB (dd/mm/yyyy)")
parts = date_input.split("/")  # create alist of strings
# my_dob = (int(parts[0]), int(parts[1]), int(parts[2]))
# print(my_dob)

# a list comprehension removes the repetition of processing parts;
# then convert list into a tuple

my_dob = tuple([int(part) for part in parts])
print(my_dob, type(my_dob))
