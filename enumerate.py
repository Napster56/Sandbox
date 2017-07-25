s = "Hello world"

for i in range(len(s)):
    print(i)

for char in s:
    print(char)

for i, char in enumerate(s):
    print("At index {:2} is {}".format(i, char))

# using a for loop
x = input("Enter a string")
y = 0
for i in x:
    print(y, i)
    y += 1

# using a enumerate function
x = input("Enter a string")
for i, char in enumerate(x):
    print(i, char)