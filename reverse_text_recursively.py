"""
Function to reverse a string recursively.

"""


def reverse(text):
    if len(text) < 2:           # base case
        return text
    else:
        # recursive step = reverse(rest of text) + first char of text
        return reverse(text[1:]) + text[0]

print(reverse("photon"))