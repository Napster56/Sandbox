def main():
    """Demo function for scope of a mutable object."""
    x = [3]  # int is immutable
    print("in main, id is {}".format(id(x)))
    function(x)
    print("in func, id is {}".format(id(x)))


# function annotations - parameter denoted by ':' and return value by '->'
def function(y: list) -> None:
    print("in func, id is {}".format(id(y)))
    y += [1]  # assignment creates a new object
    print("in func, id is {}".format(id(y)))


print(function.__annotations__)

main()


# every object is changed
# in main, id is 33994248
# in func, id is 33994248
# n func, id is 33994248
# in func, id is 33994248
