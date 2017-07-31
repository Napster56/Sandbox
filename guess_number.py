"""
Program asks the user to guess a number between 1 and 10 and keep asking until they get it right.
Uses a constant for the secret number
"""

SECRET_NUMBER = 7

num = int(input("Enter a number: "))        # priming read -> set a value for the condition to evaluste
while num != SECRET_NUMBER:
    print("Guess again: ")
    num = int(input("Enter a number: "))    # SAME as the priming read
print("You guessed correctly!")

"""
This is THE standard while loop format we want you to learn.
Note that the line before the loop header (condition) is the same as the last line of the body
"""