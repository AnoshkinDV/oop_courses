class Geom(object):
    pass
class Line(Geom):
    pass

g = Geom()
l = Line()
print(isinstance(l,Geom))
#True
print(isinstance(l,object))
#True
print(isinstance(l,Line))
#True
print(issubclass(int,object))
#True
print(issubclass(list,object))
#True

class Vector(list):
    pass
    # def __str__(self): #переопределим магический метод str
    #     return " ".join(map(str,self))
# Переопределили метод str в классе вектор
v = Vector([1,2,3,4])
print(v)
# 1 2 3 4
print(type(v))
#<class '__main__.Vector'>