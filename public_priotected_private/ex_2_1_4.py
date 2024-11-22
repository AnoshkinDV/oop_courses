class Money:
    def __init__(self, money = 0):
        if not self.__check_money(money):
            raise ValueError('Некорректное значение')
        self.__money = money

    def set_money(self, money):
        if not self.__check_money(money):
            raise ValueError('Некорректное значение')
        self.__money = money

    @classmethod
    def __check_money(cls, money):
        return type(money) is int and money >= 0

    def get_money(self):
        return self.__money

    def add_money(self, mn:"Money"):
        self.__money += mn.__money # mn это объекта класса Money а не число


mn_1 = Money(10)
mn_2 = Money(20)
mn_1.set_money(100)
mn_2.add_money(mn_1)
m1 = mn_1.get_money()
m2 = mn_2.get_money()
print(m1,m2)
