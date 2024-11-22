class Person:
    def __init__(self,name,old):
        self.__name=name
        self.__old=old
    @property
# для обращения к закрытым данным необходимы сеттеры и геттеры
    def get_old(self):
        return self.__old
    @get_old.setter
    def get_old(self,old):
        self.__old = old
    @old.deleter
    def old(self):
        del self.__old # вызывается когда происходит удаление определенного свойства
    #old = property()
    #old=old.setter(set_old)
    #old= old.getter(get_old)# приоритет обьекта свойства выше чем при обращении к приватным свойствам экземпляров класса
#они нужны чтобы не нарушалась алгоритм работы класса
p=Person('Сергей',20)
p.__dict__['old']='old in object p'
p.get_old=35
print(p.get_old, p.__dict__)
# нам нужно прописывать сетеры и гетеры для разных приватных атрибутов
