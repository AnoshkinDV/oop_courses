class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr


class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume


class MotherBoard:
    def __init__(self, name, cpu, *mem_slots): #звёздочка чтобы передать объекты произвольной длины
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        self.mem_slots = mem_slots[:self.total_mem_slots] # срез списка

    def get_config(self): # если написано что метод возвращает что-то то пишем return
        self.lst = [
            f'Материнская плата: {self.name}',
            f'Центральный процессор: {self.cpu.name},{self.cpu.fr}',
            f'Слотов памяти: {self.total_mem_slots}',
            'Память: ' + ';'.join(map(lambda x: f'{x.name} - {x.volume}',self.mem_slots))
        ]
        return self.lst
mb =  MotherBoard('GigaBayte',CPU('Intel',2000),Memory('Kingston',1000),Memory('Kingston',2000))
print(mb.__dict__)
print(mb.get_config())