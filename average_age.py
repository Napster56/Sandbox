"""
Write a program to calculate the average age of a group of people, of unknown size
Use a negative number as the 'sentinel' (when to stop)
"""

count = 0
total = 0
age = int(input("Enter your age"))
while age >0:
    count += 1
    total += age
    age = int(input("Enter your age"))
average_age = total / count
print(total, count)
print(average_age)
