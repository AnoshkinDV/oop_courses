class TVProgram:
    def __init__(self, name_channel):
        self.name_channel = name_channel
        self.items = []

    def add_telecast(self, tl):
        self.items.append(tl)

    # def remove_telecast(self,indx):
    #     for i,item in enumerate(self.items):
    #         if item.uid == indx:
    #             self.items.pop(i)
    #             break
    #Либо сделать как сергей
    def remove_telecast(self,indx):
        kort = tuple(filter(lambda x: x.uid == indx, self.items))
        for i in kort:
            self.items.remove(i)

class Telecast:
    def __init__(self,por_num,name_tl,time):
        self.__id = por_num
        self.__name = name_tl
        self.__duration = time
    @property
    def uid(self):
        return self.__id
    @uid.setter
    def uid(self,value):
        self.__id = value

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def duration(self):
        return self.__duration

    @duration.setter
    def duration(self, value):
        self.__duration = value

pr = TVProgram('Первый канал')
pr.add_telecast(Telecast(1,'Доброе утро',10000))
pr.add_telecast(Telecast(2,'Новости',2000))
pr.add_telecast(Telecast(3,'Интервью с Малаховы',20))
pr.remove_telecast(3)
for t in pr.items:
    print(f'{t.name}: {t.duration}')
