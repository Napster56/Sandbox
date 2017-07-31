"""
Program for user to create a rectangle shape
"""

from rectangle import Rectangle
rectangle = Rectangle(0, 0, 3, 2)     # four parameters are passed to __init__ constructor to create an instance of shape
rectangle.move(5, 15)                 # move method is inherited from base class
print(rectangle)
print(rectangle.area())

from circle_class import Circle

circle = Circle(3, 6, 1)
print(circle)
print(circle.area())

