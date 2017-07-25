"""
Program asks the uswr for their age, and then prints whether it is odd or even.
The program should not crash if he user enters a character other than a valid number.
The program should not crash if he user enters an invalid age number.
The user is re-prompted until a valid number is entered.
"""


def main():

    valid_input = False                # valid_number is a Boolean
    while not valid_input:             # All conditions evaluate to a Boolean
        try:                            # Therefore, valid_number is also a condition
            age = int(input("Age: "))
            if age <= 0:
                print("Age must be > 0")
            else:
                valid_input = True
        except ValueError:
            print("Invalid input; enter an integer", )

        if is_even(age):
            print("{} is even".format(age))
        else:
            print("{} is odd".format(age))


def is_even(number):        # pass number into fn as a parameter
    return number % 2 == 0   # just returns the condition but maybe less readable
    # if number % 2 == 0:
    #     return True
    # else:
    #     return False

# test code to check if correct:
# for i in range(5):
# print("{} is {}".format(i, is_even(i)))

main()                    # last line of program calls main
