# class Geom:
#     name = 'Geom'
#
#
# class Line:
#     def draw(self):
#         print("Рисование линии")
#
#
# p = Geom()
# print(p.name)
# l = Line()
# l.draw()


# Как видите, у нас здесь налицо дублирование кода. И оно будет быстро нарастать с увеличением классов для различных геометрических фигур.
# Чтобы этого не было, мы можем общее для всех дочерних классов (от Geom) вынести в базовый и, в частности, записать в нем метод set_coords.
# В итоге получим, следующие определения классов:
class Geom:
    name = 'Geom'

    def draw(self):
        print("Рисование примитива")
    def set_coords(self, x1, y1, x2, y2):
        self.x1 = x1
        self.y1 = y1
        self.x2 = x2
        self.y2 = y2


class Line(Geom):
    name = 'Line'

    def draw(self):
        print('Рисование линий')


class Rect(Geom):
    def draw(self):
        print("Рисование прямоугольника")


l = Line()
r = Rect()
l.set_coords(1, 1, 2, 2)
r.set_coords(1, 1, 2, 2)

g = Geom()
g.set_coords(0, 0, 0, 0)
print(l.name)
print(r.name)
l.draw()
r.draw()
g = Geom()
g.draw()