"""
Program to create a Rectangle class which inherits from the Shape class.
The subclass Rectangle extends the superclass Shape.
"""

from shape import Shape        # brings the base class Shape into scope


class Rectangle(Shape):        # name of base class is specified when the dericed class is defined
    def __init__(self, x=0, y=0, width=1, height=1):
        self.x = x    # redefine the __init__ with new attributes
        self.y = y    # re-declared function overrides the base class's constructor
        self.width = width
        self.height = height

    # new method only applies to Rectangle class NOT base class Shape
    def area(self):
        return self.width * self.height
