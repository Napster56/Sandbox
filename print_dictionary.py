"""
Program to print all words in a dictionary file; file has one word per line
"""

# open file named "dictionary.txt" for reading('r')
data = open("dictionary.txt", 'r')


# iterate thru the file one line at a time
# for line in data:
#    print(line)

def main():
    # main program
    print("Find words containing vowels 'aeiou' in that order: ")
    for word in data:  # for each word in file
        word = remove_whitespace(word)
        if len(word) <= 6:
            continue
        vowels = get_vowels_in_word(word)
        if vowels == "aeiou":
            print(word)


def remove_whitespace(word):
    """ return word in lowercase without whitespace"""
    return word.strip().lower()


def get_vowels_in_word(word):
    """Return vowels in word"""
    vowels = "aeiou"
    vowels_in_word = ""
    for char in word:
        if char in vowels:
            vowels_in_word += char
    return vowels_in_word

main()
