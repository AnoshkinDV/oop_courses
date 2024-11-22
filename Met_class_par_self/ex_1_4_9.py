import sys

# программу не менять, только добавить два метода
lst_in = ['1 Сергей 35 12000', '2 Федор 23 12000']  # считывание списка строк из входного потока
# lst = [chars.split() for chars in lst_in]
print(lst_in)


class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')

    def insert(self, data):

        # self.lst_data = [{k:v for k, v in zip(self.FIELDS, value.split())} for value in data] # сначала идет внешний цикл а потом внутренний
        # print(self.lst_data)

        for x in data:
            self.lst_data.append(dict(zip(self.FIELDS, x.split())))
        print(self.lst_data)

    def select(self, a, b):
        return self.lst_data[a:b + 1]

db = DataBase()
db.insert(lst_in)
db.select(1,2)
b=db.select(1,2)
print(b)
