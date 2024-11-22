class ListInteger(list):
    def __init__(self,lst):
        for x in lst:
            if isinstance(x,int):
                super().__init__(lst)
            else:
                raise TypeError('Можно передавать только целочисленные значение')
    def __setitem__(self, key, value):
        if isinstance(value,int):
            super().__setitem__(key,value)
        else:
            raise TypeError('Можно передавать только целочисленные значение')
    def append(self,value):
        if isinstance(value,int):
            super().append(value)
        else:
             raise TypeError('Можно передавать только целочисленные значение')

s = ListInteger((1,2,3))
s[1] = 10
s.append(11)
print(s)
# s[0] = 10.5

# Здесь можно указать статик метод который проверяет корректность и генерирует исключение

