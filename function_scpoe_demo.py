def main():
    """Demo function for scope of an immutable object."""
    x = 3  # int is immutable
    print("in main, id is {}".format(id(x)))
    function(x)
    print("in func, id is {}".format(id(x)))


def function(y: int):
    print("in func, id is {}".format(id(y)))
    y += 1             # assignment creates a new object
    print("in func, id is {}".format(id(y)))


main()


# reference equality
# returns: in main, id is 1396426896   }
#          in func, id is 1396426896   } sharing the same object

# after assignment y += 1:
# in main, id is 1396426896
# in func, id is 1396426896
# in func, id is 1396426928      # assignment creates a new object
