from operator import itemgetter

people = [['Bob', 38, 'e@b.com'], ['Lindsay', 42, 'a@b.com'], ['Carrie', 34, 'c@gmail.com']]

people.sort(key=itemgetter(2))  # sort by 3rd element
print(people)

people.sort(key=itemgetter(1, 0))  # sort by 2nd element then 1st element
print(people)

# Caps come before lowercase in ASCII values

strings = ["Hi", "bye", "Ho", "zap"]

strings.sort()   # sorts by first element
print(strings)

# sort by 2nd element
strings.sort(key=itemgetter(1))
print(strings)

"".join(strings)
print(strings)
