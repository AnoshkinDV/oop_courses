try:
    with open('myfile2.txt') as f:
        f.read()
except FileNotFoundError as e:
    print(e)
except Exception as z:
    print(z)


# Для примера создадим свой класс менеджера контекста, который будет менять значения вектора, и сделаем так, что
# если при изменения значений вектора произойдут ошибки то мы бы не хотели вносить эти
# изменения в конечный результат, то есть оставить его таким каким он был изначально

class DefenderVector:
    def __init__(self, v):
        self.__v = v

    def __enter__(self):  # Срабатывает в момент инициализации менеджера контекста
        self.__temp = self.__v[:]
        return self.__temp  # Возратим ссылку на копию списка

    # То есть переменная dv будет ссылаться на копию списка self.__temp
    # И далее внутри менеджера контекста мы будем работать с копией, а не с самим списком v1

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.__v[:] = self.__temp
        return False


v1 = [1, 2, 3]
v2 = [2, 3, 4]
try:
    with DefenderVector(v1) as dv:
        for i, a in enumerate(dv):
            dv[i] += v2[i]
except:
    print('Ошибка')
print(v1)
