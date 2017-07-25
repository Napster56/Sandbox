"""
input_file = open("guitar.txt", "r")
for line in input_file:
    new_line = line.strip(",")

    print(new_line, type(new_line))
    # print("My {} made in {}, cost ${:.2f}". format(new_line[0], new_line[1], new_line[2]))


input_file.close()
"""

a =[1, 2, 3]
print(type(a), id(a))
b = [1, 2, 3]
print(type(b), id(b))

# print(a == b)

# print(a is b)

print("abc" == "abc")
print("abc" is "abc")
print(123 == 123)
print(123 is 123)
print([1, 2, 3] is [1, 2, 3])
print((1, 2) == (1, 2))
print((1, 2) is (1, 2))
print({1: "a", 2: "b"} == {1: "a", 2: "b"})
print({1: "a", 2: "b"} is {1: "a", 2: "b"})