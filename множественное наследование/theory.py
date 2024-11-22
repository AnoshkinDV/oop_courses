class Goods:
    def __init__(self, name, weight, price):
        super().__init__(1) #с помощью объекта-посредника super(), которая и делегирует вызов метода __init__ класса MixinLog:
        print("init MixinLog")
        self.name = name
        self.weight = weight
        self.price = price

    def print_info(self):
        print(f"{self.name}, {self.weight}, {self.price}")


# Клас который производит логирование товаров
# Этот класс работает совершенно независимо от классов Goods и Notebook и лишь добавляет функционал
# по логированию товаров
# с использованием их id. Такие независимые базовые классы и получили название миксинов – примесей.
class MixinLog:
    ID = 0

    def __init__(self,p1):
        print("init MixinLog")
        self.ID += 1
        self.id = self.ID

    def save_sell_log(self):
        print(f"{self.id}: товар продан в 00:00 часов")


class NoteBook(Goods, MixinLog):
    pass


n = NoteBook("Acer", 1.5, 30000)
n.print_info()
n.save_sell_log()
# init MixinLog
# Acer, 1.5, 30000
# AttributeError: 'NoteBook' object has no attribute 'id'. Did you mean: 'ID'?
#Ошибка связанная с тем что не был вызван инициализатор класса MixinLog\

#Чтобы увидеть цепочку обхода базовых классов , распечатаем коллекцию mro
print(NoteBook.__mro__)
# (<class '__main__.NoteBook'>, <class '__main__.Goods'>, <class '__main__.MixinLog'>, <class 'object'>)
