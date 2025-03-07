class RealValue:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]


class Point:
    x = RealValue()
    y = RealValue()

    def __init__(self, x, y):
        self.x = x
        self.y = y
pt = Point(1.5,2.3)
pt.__dict__['x'] = 10.0
print(pt.x)
# Ответ 10 тк как ReakValue это дескриптор не данных и в инициализаторе будут созданы локальные свойства x,y
# Затем в строчке pt.x идет обращение к локальному свойству x со значением 10

class StringField:
    def __set_name__(self, owner, name):
        self.name = '_' + name

    def __get__(self, instance, owner):
        return instance.__dict__[self.name]

    def __set__(self, instance, value):
        instance.__dict__[self.name] = value


class DataBase:
    x = StringField()
    y = StringField()

    def __init__(self, x, y):
        self.x = x
        self.y = y

db = DataBase('hi','low')
db.__dict__['x'] = 'top'
print(db.x)

#Будет выведено hi так StringField это дескриптор данных и он имеет наибольший приоритет при обращении к атрибутам,
#поэтому в строчке db.x идет обращение к дескриптору, а не к локальному свойству
#hi