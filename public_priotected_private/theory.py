
class Point:
    def __init__(self,x=0,y=0):
        self.__x = self.__y = 0
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
    # Добавим приватный метод класа для проверки корректности введенных коодинат
    @classmethod
    def __check_value(cls,x):
        return type(x) in (int,float) # в одном месте можем проводить проверки для допустимости координат точек

    def set_coord(self,x,y): # внутри класса мы можем обращаться к публичным атрибутом, но извне нельзя
        if self.__check_value(x) and self.__check_value(x):
            self.__x = x
            self.__y = y
        else:
            raise ValueError('Координаты должны быть числами')
    def get_coord(self):
        return self.__x,self.__y
    #Теперь в классе появились  методы которые работает с защищенными атрибутами - setter и getter
# Тепрь у нас в программе существуют приватные локальные свойства и один приватный метод check_value
pt = Point(1,2)
pt.set_coord(10,20)
print(pt._Point__x)