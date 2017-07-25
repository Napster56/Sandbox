"""Program to use Point class """

from point import Point

# points = [Point(), Point(), Point()]
point = Point()  # This executes Point __init__()
print(point)

points = [Point(2, 2), Point(4, 4), Point(4, 0)]

i = 0
for point in points:
    point.move(i, i)
    i += 1

for point in points:
    point(point, end="")

print(point)
