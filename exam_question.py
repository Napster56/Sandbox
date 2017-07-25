"""
Program to compute highest, lowest, average
"""

rainfall = [15, 10, 23, 43, 10, 78, 90]
highest = rainfall[0]
lowest = rainfall[0]
for value in rainfall:
    if value > highest:
        highest = value
    if value < lowest:
        lowest = value
average = sum(rainfall) / len(rainfall)
print("lowest {}, highest {} and average {:.1f}".format(lowest, highest, average))

# insert method for list
things = [2, "Bob", 34.2, [2,3], True]
things.reverse()
print(things)
things.insert(2, "Hi")
print(things)

# append & extend methods
things.append("Low")    # appends a string "Low"
print(things)

things.extend("Low")    #extends as "L", "o", "w"
print(things)

# pop method
new_things = things.pop()      # If no index is specified, a.pop() removes
print(new_things)              # and returns the last item in the list.
print(things)
new_things = things.pop(2)     # Remove the item at the given position in the list,
print(new_things)                  #  and return it.
print(things)

# sort method --> elements must be homogeneous type; sort retutns none
things2 = [12, 3, 45, 678, 48]
things2.sort()
print(things2)
things3 = things2.sort()      # sort doesn't return a value; return None by default
print(things3)                # prints --> None

strings = ["Hi", "bye", "Ho", "zap"]
strings.sort()                # sort doesn't return a value: modifies list directly
print(strings)

things.sort()
print(things)
"""
File "F:/CP1404 Programming I/Sandbox/exam_question.py", line 22, in <module>
[2, 'Bob', 'Hi', 34.2, [2, 3], True]
    things.sort()
TypeError: unorderable types: str() < int()
"""




