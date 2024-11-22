class RadiusVector2D:
    # def __new__(cls, *args, **kwargs):
    #     cls.MIN_COORD = -100
    #     cls.MAX_COORD = 1024
    MIN_COORD = -100
    MAX_COORD = 1024

    def __init__(self, x=0, y=0):
        self.__x = self.__y = 0
        if type(x) in (int, float) and self.MIN_COORD <= x <= self.MAX_COORD:
            self.__x = x
        if type(y) in (int, float) and self.MIN_COORD <= y <= self.MAX_COORD:
            self.__y = y

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) in (int, float) and self.MIN_COORD <= value <= self.MAX_COORD:
            self.__y = value

    @staticmethod
    def norm2(vector):
        return vector[0] ** 2 + vector[1] ** 2


v1 = RadiusVector2D()
v2 = RadiusVector2D(12020, 202020)
v3 = RadiusVector2D(1, 2)
res = RadiusVector2D.norm2([v3.x, v3.y])
print(res)
print(v1.x, v1.y)
print(v2.x, v2.y)
v2.x, v2.y = 10, 10
print(v3.x, v3.y)
print(v2.x, v2.y)
