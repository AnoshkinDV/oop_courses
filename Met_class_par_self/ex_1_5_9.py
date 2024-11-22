import sys


class ListObject:
    def __init__(self,data):  # принимает один аргумент строку которую сохраняем в локальном атрибуте объкета класса ListObj
        self.next_obj = None  # ссылка на следующий объект класса ListObj, по умолчанию None
        self.data = data

    def link(self, obj):  # если мы присоединяем к текущем объекту новый object
        self.next_obj = obj



# lst_in = list(map(str.strip, sys.stdin.readlines())) # список lst_in в программе не менять

# head_obj = ListObjcet(lst_in[0]) # формируется первый объект
# Сформируем вспомогательную переменную (указатель) которая будет указывать изначально не первй созданные объект

# А затем переберем все оставшиеся строки

# obj = head_obj
# for i in range(1,len(lst_in)):
#     obj_new = ListObjcet(lst_in[i])
#     # эти новые создаваемые объекты нужно соединять друг с другом
#     obj.link(obj_new) # таким образом obj будет соеденен с obj new
#     obj = obj_new

obj1 = ListObject(['jjj','jjfjfj','mgmgm'][0])
obj = obj1
for x in ['jjj','jjfjfj','mgmgm'][1:]:
    new_obj = ListObject(x)
    obj1.link(new_obj)

print(obj)
