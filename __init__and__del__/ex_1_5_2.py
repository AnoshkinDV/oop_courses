class Money:
    def __init__(self,money): # ссылка на экземпляр класса для к-го вызывается инит
        self.money = money

my_money = Money(100)
your_money = Money(1000)