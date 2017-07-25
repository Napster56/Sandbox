""""""

choice =input("Choose a, b, c or d")
"""
while choice not in ["a", "b", "c", "d"]:
    print("Invalid input")
    choice = input("Choose a, b, c or d")

# below allows inputs like "ab" and "bcd"
while choice not in "abcd":
    print("Invalid input")
    choice = input("Choose a, b, c or d")
"""


# below is a safe alternative to first using the list constructor list()
# the list constructor splits "abcd" into single characters
while choice not in list("abcd"):
    print("Invalid input")
    choice = input("Choose a, b, c or d")


