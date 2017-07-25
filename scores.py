"""
Program asks user for their scores and adds them to the list,
until they enter a negative score, then prints their highest score.
"""
"""                                        # Pseudocode
scores = []                               # scores = empty list
score = int(input("Score: "))             # get score from user, repeat until
while score >= 0:                         # user enters a negative number
    scores.append(score)                  # add score to list
    score = int(input("Score: "))         # get score from user
print("Your highest score is", max(scores))  # find and display max score

# program will crash if user enters a negative number first because list is empty
# and there is no max
"""
scores = []                               # scores = empty list
  # get score from user, repeat until
score = int(input("Score: "))
while score >= 0:                         # user enters a negative number
    try:
        if score < 0:
            my_error = ValueError
            raise my_error
        else:
            scores.append(score) # get score from user

    except ValueError:
        print("Invalid input")
        score = int(input("Score: "))

    print("Your highest score is", max(scores))
