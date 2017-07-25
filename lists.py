
# create list using the constructor;
# splits string into elements and adds each letter to list
my_list = list("Hello")
print(my_list)

my_list = list("1234")
print(my_list)

# constructor takes only iterable data structure; int is not iterable!!!
# my_list = list(1)
print(my_list)


# create list using the shortcut
my_list = ["Hello"]
print(my_list)

my_list = [1, 2, 3, 4]
print(my_list)

# slicing for every 2nd element
print(my_list[::2])

# membership using the in operator
print(4 in my_list)

name_list = list("Lindsay")
print(name_list)

print("ds" in name_list)

print(name_list == [])  # check if list is emplty

# remove l;ast element with pop operator
my_list.pop(2)
print(my_list)

# reverse order
print(my_list.reverse())  # a list normally returns none
new_list = my_list.reverse()

print(new_list)

myList = [1, 'a', 3.15159, True]
print(myList[:3])     # slicing doesn't include the last element!!!!!

# list of lists
my_list = ['a', [1, 2, 3], 'z']
print(my_list[1][1])
print(my_list[1])