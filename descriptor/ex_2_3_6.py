class FloatValue:
    @classmethod
    def verify_float(cls, coord):
        if type(coord) != float:
            raise TypeError('Присваивать можно только вещественный тип данных')

    def __set_name__(self, owner, name):
        self.name = '_' + name

    # Это геттер
    def __get__(self, instance, owner):  # instance это ссылка на созданный экземпляр класса pt=Point()
        # правильнее писать
        return getattr(instance, self.name)

    # Это сеттер
    def __set__(self, instance, value):
        print(f'__set__:{self.name} = {value}')
        self.verify_float(value)
        # правильнее писать
        setattr(instance, self.name, value)


class Cell:
    value = FloatValue()

    def __init__(self, value=0.0):
        self.value = value


class TableSheet:
    def __init__(self, N, M):
        self.N = N
        self.M = M
        self.cells = []
        t = 0.0
        for i in range(self.M):
            self.cells.append([])
            for _ in range(self.N):
                self.cells[i].append(Cell(t))
                t += 1
table = TableSheet(5,3)
print(table.cells)