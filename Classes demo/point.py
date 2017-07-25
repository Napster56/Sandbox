
"""Program to create a Point class where a point has coordinates (x,y)
 on a Cartesian plane"""


class Point():
    # __init__ is constructor method
    # This is how I create a new point
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    # __str__ is getter method
    # This is how I get the value of the data
    def __str__(self):
        return"({}, {})".format(self.x, self.y)

    def move(self, dx, dy):
        # translation function defines behaviour of point (objects)
        self.x = self.x + dx
        self.y = self.y + dy

    def reset(self):
        self.x = 0
        self.y = 0




