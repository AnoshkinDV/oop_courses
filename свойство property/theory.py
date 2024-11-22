class Person:
    def __init__(self, name, old):
        self.__name = name
        self.__old = old
    @property # перед гетером ставится декоратор property
    def old(self):
        return self.__old
    @old.setter
    def old(self,old):
        self.__old = old
    @old.deleter
    def old(self):
        del self.__old

p = Person('Сергей',20)
del p.old
# p.__dict__['old'] = 'old in object p'
p.old = 35
print(p.__dict__)