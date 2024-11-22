class Point:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        if color is None:
            self.color = 'black'
        else:
            self.color = color


points = []
for i in range(0,1001, 2):
    points.append(Point(i, i))
points[1].color = 'yellow'
for point in points:
    print(point.x, point.y, point.color)
# либо points=[Point(2*i+1,2*i+1) for i in range(0,1000)]
