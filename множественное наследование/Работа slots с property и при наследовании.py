class Point2D:
    __slots__ = ('x','y')


class Point3D(Point2D):
    __slots__ = 'z',

    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
