class ObjList:
    def __init__(self, data):
        self.__next = None
        self.__prev = None
        self.__data = data

    def set_next(self, obj):
        self.__next = obj

    def set_prev(self, obj):
        self.__prev = obj

    def get_next(self):
        return self.__next

    def get_prev(self):
        return self.__prev

    def set_data(self):
        return self.__data

    def get_data(self):
        return self.__data

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add_obj(self,obj):

        # Если tail равен None(список пуст)
        if self.tail: # можем так делать если tail ссылается на существующий объект, а у нас может быть изначально пустой список
            self.tail.set_next(obj)
        obj.set_prev(self.tail)
        self.tail = obj # Переопределение атрибутов head tail
        if self.head is None: #  Если head равен None
            self.head = obj
    def remove_obj_last(self):
        if self.tail is None:# то есть нет вообще никаких объектов
            return
        prev = self.tail.get_prev() # get prev возвращает ссылку на предыдущий объект

        if prev: # если prev существует, то есть prev может быть None, например удаляем единственный объект из списка, то есть он ни на что не ссылается
            prev.set_next(None) #Делаем что next указывал на None

        self.tail = prev
        # Если мы удаляем один единственный 1ый объект, то у нас tail будет указывать на None, и head должен указывать на None
        if self.tail is None:
            self.head = None
    def remove_obj_first(self):
        if self.head is None:
            return
        ptr = self.head.get_next()
        if ptr:
            ptr.set_prev(None)
        self.head = ptr
        if self.head is None:
            self.tail = None

    def get_data(self):
        sps = []
        h = self.head
        while h: # пока h не равен None
            sps.append(h.get_data())
            h = h.get_next() # Переходим на следующий объект связного списка, так как get next возвращает ссылку на след объект, то есть h ссылается уже на след объект
        return sps

lst = LinkedList()

lst.add_obj(ObjList('Данные 1'))
lst.add_obj(ObjList('Данные 2'))
# lst.add_obj(ObjList('Данные 3'))
# lst.add_obj(ObjList('Данные 4'))
lst.remove_obj_first()
res = lst.get_data()
print(res)