class Thing:
    __id_counter = 0
    __attrs = ('id','name','price','weight','dims','memory','frm')
    def __init__(self, name = None, price = None):
        Thing.__id_counter += 1
        self.id = Thing.__id_counter
        self.name = name
        self.price = price
        # self.weight = None
        # self.dims = None
        # self.memory = None
        # self.frm = None
        # Можно через множественное присваивание
        self.weight = self.dims = self.memory = self.frm =None
    #Можно это сделать через класс метод
    # @classmethod
    # def __get_id(cls):
    #     Thing.__id_counter +=1
    #     return  Thing.__id_counter

    def get_data(self):
        return (self.id,self.name,self.price,self.weight,self.dims,self.memory,self.frm)
    # Можно это сделать через генератор
    #     return tuple(getattr(self,name) for name in self.__attrs)


class Table(Thing):
    def __init__(self, name, price, weight=None, dims=None):
        super().__init__(name, price)
        self.weight = weight
        self.dims = dims


class ElBook(Thing):
    def __init__(self, name, price, memory=None, frm=None):
        super().__init__(name, price)
        self.memory = memory
        self.frm = frm

table = Table('Круглый',1024,812.55,(700,750,700))
book = ElBook('Python ООП',2000,2048,'PDF')
print(*table.get_data())
print(*book.get_data())