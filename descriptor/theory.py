class ReadIntX:
    def __set_name__(self, owner, name):
        self.name = '_x'

    def __get__(self, instance, owner):
        return getattr(instance, self.name)


class Integer:
    @classmethod
    def verify_coord(cls, coord):
        if type(coord) != int:
            raise TypeError('Координаты должны быть целыми числами')

    # Это чтобы сформировать локальное свойство через которое потом будем обращаться в геттере и сеттере
    def __set_name__(self, owner,
                     name):  # self ссылка на экземляр класса Integer, owner ссылка на класс Point3D, name это имя локальной переменной
        self.name = '_' + name

    # Это геттер
    def __get__(self, instance, owner):  # instance это ссылка на созданный экземпляр класса pt=Point()
        # return instance.__dict__[self.name]
        # правильнее писать
        return getattr(instance, self.name)

    # Это сеттер
    def __set__(self, instance, value):
        print(f'__set__:{self.name} = {value}')
        self.verify_coord(value)
        # instance.__dict__[self.name] = value
        # правильнее писать
        setattr(instance, self.name, value)


# Такова простейшая реализация дескриптора
class Point3D:
    # В самом классе сформируем интерфейсы взаимодействия с нашими координатами
    x = Integer()
    y = Integer()
    z = Integer()
    xr = ReadIntX()  # создали дексриптор не данных

    def __init__(self, x, y, z):
        self.x = x  # когда выполняем это то вызывается соответсвующий сеттер и формируется локальное свойство при чем с проверкой
        self.y = y
        self.z = z

    # @property
    # def x(self):
    #     return self.__x
    # @x.setter
    # def x(self,coord):
    #     self.verify_coord(coord)
    #     self.__x = coord
    #
    # @property
    # def x(self):
    #     return self.__x
    #
    # @x.setter
    # def x(self, coord):
    #     self.verify_coord(coord)
    #     self.__x = coord
    #
    # @property
    # def y(self):
    #     return self.__y
    #
    # @x.setter
    # def y(self, coord):
    #     self.verify_coord(coord)
    #     self.__y = coord
    #
    # @property
    # def z(self):
    #     return self.__z
    #
    # @x.setter
    # def z(self, coord):
    #     self.verify_coord(coord)
    #     self.__z = coord


p = Point3D(1, 2, 3)
p.__dict__['xr'] = 5  # Мы просто создали локальный атрибут со значением 5
# 5 {'_x': 1, '_y': 2, '_z': 3, 'xr': 5} 3
print(p.xr, p.__dict__, p.z)
# __set__:_x = 1
# __set__:_y = 2
# __set__:_z = 3
# {'_x': 1, '_y': 2, '_z': 3}
# По итогу мы имеем сделали универсальную проверку для всех трех координат, и к тому же мы имеем универсальное описание интерфейса работы с этими координатами
