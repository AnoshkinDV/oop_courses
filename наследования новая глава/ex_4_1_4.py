class Animal:
    def __init__(self, name, old):
        self.name = name
        self.old = old


class Cat(Animal):
    def __init__(self, name, old, color, weight):
        Animal.__init__(self,name, old)
        self.color = color
        self.weight = weight

    def get_info(self):
        print(f'{self.name}: {self.old}, {self.color}, {self.weight}')


class Dog(Animal):
    def __init__(self, name, old, breed, size):
        Animal.__init__(self,name, old)
        self.breed = breed
        self.size = size

    def get_info(self):
        print(f'{self.name}: {self.old}, {self.breed}, {self.size}')


cat = Cat('Семён', 4, 'Серый', 2.25)
dog = Dog('Барбос', 2, 'Овчарка', [2, 2])
cat.get_info()
dog.get_info()
