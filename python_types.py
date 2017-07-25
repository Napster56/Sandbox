things = [1, 0.2, "hi", (1, "a"), {1: 4}]
for thing in things:
    print("{:8} is {}".format(repr(thing), type(thing)))
print("{:8} is {}".format(repr(things), type(things)))

my_string = "pixie"
print(my_string.upper())

