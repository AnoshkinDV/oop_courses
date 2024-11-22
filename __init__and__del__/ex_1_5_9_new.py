# Создаем класс
class ListObject:
    head_obj = None

    def __init__(self, data):
        self.data = data
        self.next_obj = None

    def link(self, obj):
        self.next_obj = obj


lst_in = ['1','2','3']
head_obj = ListObject(lst_in[0])
obj = head_obj
for x in lst_in[1:]:
    new_obj = ListObject(x)
    obj.link(new_obj)
    obj = new_obj
print(obj)