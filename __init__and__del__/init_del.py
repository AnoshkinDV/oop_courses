class Point:
    "Класс для представления координат точек на плоскости"
    color = 'red'
    circle = 2  # атрибуты класса Point

    def __init__(self, x = 0, y = 0):
        print('вызов __init__')
        self.x = x  # создаем два локальных свойства
        self.y = y

    def __del__(self):
        print('Удаление экземляра:' + str(self))

    def set_coords(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def get_coords(self):
        return self.x, self.y


pt = Point(1)
print(pt.__dict__)
