class Point:
    def __new__(cls, *args, **kwargs):
        print('Вызов __new__ для' + str(cls))
        return super().__new__(cls)

    def __init__(self, x=0, y=0):
        print('Вызов __init__ для' + str(self))
        self.x = x
        self.y = y


pt = Point(1, 2)  # экземпляр класса не был создан
print(pt)


# Реализация класса DataBase с учетом патерна SingleTon, то есть программист может создаваить только один экземпляр класса,должен создаваться 1 объект
class DataBase:
    __instance = None  # ссылка на экземпляр класса

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:  # если атрибут инстанс принимает значение None то тогда мы в этой строчке создаем новый экземпляр класа
            cls.__instance = super().__new__(cls)
        return cls.__instance  # возвращаем адрес ранее созданного объекта
    # В методе init мы каждый раз создаем или изменяем локальные свойства,чтобы этого не было, нужен еще один магический метод call
    def __init__(self, user, psw, port):
        self.user = user
        self.psw = psw
        self.port = port

    def __del__(self):
        DataBase.__instance = None

    def connect(self):
        print(f'Соединение с БД:{self.user},{self.psw},{self.port}')

    def close(self):
        print('Закрытие соединения с БД')

    def read(self):
        return 'Данные из БД'

    def write(self, data):
        print(f'Запись в БД {data}')


db = DataBase('root', '1234', 80)
db2 = DataBase('root2','5678',40)
print(id(db),id(db2)) # id одинаковые то есть при попытке создании нового обьекта он не был создан
print(db.user)
print(db2.user)