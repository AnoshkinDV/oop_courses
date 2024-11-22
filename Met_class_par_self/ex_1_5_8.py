class Cart:
    def __init__(self):
        self.goods = []

    def add(self, gd):
        self.goods.append(gd)

    def remove(self, indx):
        del self.goods[indx]

    def get_list(self):
        return [f'{x.name}:{x.price}' for x in self.goods]


class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price


class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price


cart = Cart()
cart.add(TV('Самсунг', 12000))
cart.add(TV('LG', 12000))
cart.add(Table('Плотник', 5000))
cart.add(Notebook('ASUS', 50000))
cart.add(Notebook('Huawey', 75000))
cart.add(Cup('Кружка', 500))
print(cart.get_list())
# def foo(lst):
#     v_min=min(lst)
#     v_max=max(lst)
#     v_sum=sum(lst)
#     print(f'Min = {v_min}, max = {v_max}, sum = {v_sum}')
# foo(list(map(int,input().split())))
#
# def foo(width,height):
#     x=2*width+2*height
#     print(f'Периметр прямоугольника, равен {x}')
# foo(*map(int,input().split()))
#
# def foo(email):
#     for i,char in enumerate(email):
#         if char == '@' and char == '.':
#             print('ДА')
#     else:
#         print('НЕТ')
# foo(input())
#
# def foo(x):
#     return True if x%2==0 else False
# x = int(input())
# while x!=1:
#     if foo(x):
#         print(x)
#     x = int(input())
# def foo(x):
#     return True if x%2!=0 else False
# lst_d = list(map(int, input().split()))
# lst=[x for x in lst_d if foo(x)]
# print(*lst)
#
# if tp=='RECT':
#     def get_sq(a,b):
#        return a*b
# else:
#     def get_sq(a):
#         return a*a
#
# def foo(str):
#     return  len(str)>=6
# lst=[x for x in input().split() if foo(x)]
# print(*lst)
#
#
# def foo(str):
#     return str, len(str)
#
#
# cities = [x for x in input().split()]
# d = {x: y for (x, y) in (foo(x) for x in cities)}
# a = sorted(d, key=d.get)
# print(*a)
# #b = tuple(foo(x) for x in cities)
# #print(b)
# digs=[x for x in map(int,input().split())]
# def min_max(x,y):
#     return x*y
# print(min_max(max(digs),min(digs)))
