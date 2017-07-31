"""

User program to make a shape.
"""

from shape import Shape

shape = Shape(0, 0)
shape.move(10, 10)
print(shape, '\n', type(shape), '\n', type(Shape))
