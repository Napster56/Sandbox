"""
Program to create a Circle class which inherits from the Shape class.
The subclass Circle extends the superclass Shape; Circle 'is-a' Shape.

"""

from shape import Shape


class Circle(Shape):
    def __init__(self, x=0, y=0, radius=1):
        super().__init__(x, y)   # used to access the instance of the Shape class
        self.radius = radius     # redefines the __init__ with a new instance variable

    def area(self):
        from math import  pi
        return self.radius ** 2 * pi
