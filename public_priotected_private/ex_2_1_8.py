class Point:
    def __init__(self, x, y):
        if self.__check_value(x, y):
            self.__x, self.__y = x, y

    def get_coords(self):
        return self.__x, self.__y

    @classmethod
    def __check_value(cls, x, y):
        return type(x) in (int, float) and type(y) in (int, float)


class Rectangle:
    def __init__(self, x1, y1, x2 , y2 : 'Point' ):  # если параметр x1 и y1 является объектом класса Point то формируем прямоугольник
            self.__sp = Point(x1, y1)  # явно формируем объекты класса Point
            self.__ep = Point(x2, y2)

    def set_coords(self, sp, ep):
        self.__sp = sp
        self.__ep = ep

    def get_coords(self):
        return self.__sp, self.__ep

    def draw(self):
        print(f'Прямоугольник с координатами:{self.__sp.get_coords()} {self.__ep.get_coords()}')
        # Здесь мы вызываем метод get_coords для объекта Point(у нас есть два метода get) для объектов класа Point и для класса Rectangle


rect = Rectangle(0, 0, 20, 34)
# rect.set_coords(Point(1,2),Point(3,4))
rect.draw()
