import timeit


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calc(self):
        self.x +=1
        del self.y
        self.y = 0

class Point2D:
    __slots__ = ('x','y')
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def calc(self):
        self.x +=1
        del self.y
        self.y = 0


p = Point(1,2)
p2 = Point2D(10,20)

t1 = timeit.timeit(p.calc) #  Передаем ссылку на метод calc а не вызываем
t2 = timeit.timeit(p2.calc)
print(t1,t2)
#0.16117019997909665 0.1443672999739647
