class Thing:
    def __init__(self,name,price,weight):
        self.name = name
        self.price = price
        self.weight = weight

    #Для каждого уникального набора данных name,price,weight должны формироваться уникальные ключи

    def __hash__(self):
        return hash((self.name, self.price, self.weight))

class DictShop(dict):
    def __init__(self, things = None):
        things = {} if things is None else things
        if not isinstance(things,dict):
            return TypeError('аргумент должен быть словарем')
        if not all(isinstance(thing, Thing) for thing in things):
            raise TypeError('Ключами могут быть только объекты клаcса Thing')
        super().__init__(things)
    def __setitem__(self, key,  value):
        if not isinstance(key, Thing):
            raise TypeError('Ключами могут быть только объекты клаcса Thing')
        super().__setitem__(key,value)

th_1 = Thing('Лыжи',1100,1978.55)
th_2 = Thing('Книга',1500,256)
dict_things = DictShop()
dict_things[th_1] = th_1
dict_things[th_2] = th_2
for x in dict_things:
    print(x.name)

# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]
# print(lst_in)
# #[[1, 2, 3, 4], [5, 6, 7, 8], [9, 8, 7, 6], [5, 4, 3, 2]]
# lst_new = [x for row in lst_in[::-1] for x in row[::-1]]
# str = ' '.join(map(str,lst_new))
# print(str)
#1 2 3 4
# 5 6 7 8
# 9 8 7 6
# 5 4 3 2

# lst = list(map(int,input().split()))
# k = int(len(lst)**0.5)
# lst_n = [lst[i*k:i*k+k] for i in range(k)]
# print(lst_n)

# t = ["– Скажи-ка, дядя, ведь не даром",
#     "Я Python выучил с каналом",
#     "Балакирев что раздавал?",
#     "Ведь были ж заданья боевые,",
#     "Да, говорят, еще какие!",
#     "Недаром помнит вся Россия",
#     "Как мы рубили их тогда!"
#     ]
#
# lst = [[x for x in st.split() if len(x)>3] for st in t]
# print(lst)

# import sys
# s = sys.stdin.readlines()
# lst_in = [list(map(int, x.strip().split())) for x in s]

# A_TP = [[row[i] for row in lst_in] for i in range(len(lst_in[0]))]
# for row in A_TP:
#     print(*row)
#
# for i in range(len(lst_in[0])):
#     print(i)
#     for row in lst_in:
#         print(row[i]) # row это каждый вложенный список и у каждого этого вложенного списка берем i индекс
# rows = len(lst_in)
# cols = len(lst_in[0])
# lst_out = [[lst_in[i][j] for j in range(cols)] for i in range(rows)]
# print(lst_out)


class Point:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __hash__(self):
        return hash((self.x,self.y))