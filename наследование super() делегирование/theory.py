# class Geom:
#     name = 'Geom'
#
# class Line(Geom):
#     def draw(self): # Это расширение
#         print("Рисование линии")
#
# class Geom:
#     name = 'Geom'
#     def draw(self):
#         print("Рисование примитива")

# class Line(Geom):
#     def draw(self): # Это переопределение метода draw
#         print("Рисование линии")

# class Geom:
#     name = 'Geom'
#     def __init__(self):
#         print('инициализатор Geom')
# class Line(Geom):
#     def draw(self):
#         print("Рисование линии")
#
# l = Line()
#инициализатор Geom

class Geom:
    name = 'Geom'
    def __init__(self,x1,y1,x2,y2):
        print(f'инициализатор Geom для {self.__class__}')
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2
class Line(Geom):
    def draw(self): # Это переопределение метода draw
        print("Рисование линии")
#Добавим еще один дочерний класс Rect
class Rect(Geom):
    def __init__(self,x1,y1,x2,y2,fill = None):
        super().__init__(x1,y1,x2,y2)
        print('инициализатор Rect')
        self.fill = fill
    def draw(self): # Это переопределение метода draw
        print("Рисование прямоугольника")
# Происходит дублирование кода, вынесем в базовый класс общее
l = Line(0,0,10,20)
r = Rect(1,2,3,4)
#инициализатор Line

print(r.__dict__)
#{'x1': 0, 'y1': 0, 'x2': 10, 'y2': 20}