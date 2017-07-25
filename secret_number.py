"""
Program asks the user for a number between 1 and 10
"""
PROMPT = "Enter your guess: "     # string literal
SECRET_NUMBER = 7                 # integer literal

user_guess = int(input(PROMPT))  # get initial loop control variable from user

while user_guess != SECRET_NUMBER:
    print("Guess again")
    user_guess = int(input(PROMPT))
print("You guessed correctly; {} is the secret number!".format(SECRET_NUMBER))