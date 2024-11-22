class Car:
    def __init__(self):
        self.__model = None
    @property # реализуется объект свойство с именем model для записи и считывания информации о модели из локальной приватной переменной __model
    def model(self):
            return self.__model
    #Обьект свойство объявляется с помощью декоратора property


    @model.setter
    def model(self, car):
        if type(car) is str and 2 <= len(car) <= 100:
            self.__model = car

car = Car()
car.model = 'Toyota'
car = car.model
print(car)