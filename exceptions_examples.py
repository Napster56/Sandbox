""" Demo of non-local exception catching. """

"""
def main():
    # local catching version
    print("Hello")
    while True:
        try:
            age = int(input("Age: "))
            while age <= 0:             # age must be > 0
                print("Invalid age")
                age = int(input("Age: "))
        except ValueError:
            print("Invalid age")
        else:                   # executes only if no exception
            print("You are {} years old".format(age))
            break   # exits program

main()
"""

def non_local():
    # non-local catching version
    print("Hello")
    while True:
        try:
            age = get_age()
            while age <= 0:             # age must be > 0
                print("Invalid age")
                age = int(input("Age: "))
        except ValueError:
            # the exception generated inside the function is caught here
            print("Invalid age... using 0")
            age = 0
        else:
            print("You are {} years old".format(age))
            break


def get_age():
   # the exception is generated here and not handled
    # it is passed out of the function
    return int(input("Age: "))

non_local()

