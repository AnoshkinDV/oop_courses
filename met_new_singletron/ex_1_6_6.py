# class AbstractClass():
#     def __new__(cls, *args, **kwargs): # за создание экз-ра класса отвечает маг метод new
#         return 'Нельзя создавать объекты данного класса'
# obj = AbstractClass()
# print(obj)

class SingletonFive:
    __num = 0
    __instance = None  # ссылается на последний созданный экземпляр класса

    def __new__(cls, *args, **kwargs):  # контролирует процесс создания объектов класса
        if cls.__num <= 5:  # если атрибут инстанс принимает значение None то тогда мы в этой строчке создаем новый экземпляр класа
            cls.__instance = super().__new__(cls)
            cls.__num += 1
        return cls.__instance

    def __init__(self, name):
        self.name = name
objs = [SingletonFive(str(n)) for n in range(10)] # эту строчку не менять