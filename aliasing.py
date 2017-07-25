"""
Be aware that an assignment statement does not copy a list...
An assignment statement only creates a new variable that refers to the existing list
"""

numbers = [10, 20, 30]
things = numbers
numbers.append(40)
print(numbers, id(numbers), type(numbers))
print(things, id(things), type(things))

# [10, 20, 30, 40] 14008584 <class 'list'>
# [10, 20, 30, 40] 14008584 <class 'list'>