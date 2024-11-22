class Vector:
    MIN_COORD=0
    MAX_COORD=100
    @classmethod
    def validate(cls,arg):#параметр cls ссылка на текущий класс Vector
        return cls.MIN_COORD <= arg <= cls.MAX_COORD
    #метод класса работает исключительно с атрибутами класса Vector, но не может обращаться к локальным атрибутам экземпляра класа
    def __init__(self,x,y):
        self.x=self.y=0
        if self.validate(x) and self.validate(y):# проверим значения допустимы или нет
            self.x=x
            self.y=y# вместо .Vector можно написать .self, тк это ссылка на текущий экземляр класса и также содержит информацию о классе

        print(self.norm2(self.x,self.y))
    def get_coord(self):
        return self.x,self.y
    @staticmethod
    def norm2(x,y): #нет доп параметров
        return x*x+y*y
v=Vector(10,20)
print(Vector.norm2(5,6))
res=Vector.get_coord(v) # здесь мы обязаны указать ссылку self  на экземляр класса
print(res)


