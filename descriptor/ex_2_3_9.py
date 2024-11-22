class Bag:
    def __init__(self,max_weight):
        self.max_weight = max_weight
        self.__things = []
        self.weights = 0
    @property
    def things(self):
        return self.__things

    def add_things(self,thing):
        if self.weights + thing.weight < self.max_weight: # если текущий вес + вес который мы хотим добавить будет больше то ничего не произойдет и текующая сумма не изменится
            self.weights += thing.weight
            self.__things.append(thing)

    def remove_thing(self,indx):
        if self.things:
            self.__things.pop(indx)

    def get_total_weight(self):
       return self.weights

class Thing:
    def __init__(self,name,weight):
        self.name = name
        self.weight = weight



bag = Bag(1000)
bag.add_things(Thing('Книга по Python',100))
bag.add_things(Thing('Котелок',500))
bag.add_things(Thing('Спички',20))
bag.add_things(Thing('Бумага',100))
bag.add_things(Thing('Бумага',500))
w = bag.get_total_weight()
for t in bag.things:
    print(f'{t.name}:{t.weight}')
print(w)
#Таким образом, get_total_weight будет возвращать только ту сумму, которая была посчитана с учетом максимального веса.