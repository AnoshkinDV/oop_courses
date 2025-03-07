class Vector:
    MIN_COORD = 0
    MAX_COORD = 100
    @classmethod
    def validate(cls,arg):
        return cls.MIN_COORD <= arg <= cls.MAX_COORD # метод класса который делает проверку

    def __init__(self,x,y):
        self.x = self.y = 0
        if  self.validate(x) and self.validate(y):
            self.x = x
            self.y = y
        print(self.norm2(self.x,self.y))
    def get_coord(self):
        return self.x,self.y

    @staticmethod
    def norm2(x,y): # нет скрытых параметров
        return x*x + y*y +Vector.MAX_COORD

v = Vector(1,2)
print(Vector.validate(5)) # вызываем без доп ссылок
print(Vector.norm2(5,6))
res = Vector.get_coord(v) # v ссылка на экземпляр класса
print(res)