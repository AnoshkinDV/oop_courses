class SingleTon:
    __instance = None # с помощью него мы будем контролировать создан ли объект класса или нет

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None: # если None то мы не создавали еще объект этого класа
            cls.__instance = object.__new__(cls)
        return cls.__instance


class Game(SingleTon):
    def __init__(self, name):
        if 'name' not in self.__dict__:
            self.name = name


g1 = Game('Варкрафт')
g2 = Game('Дота 2')
print(id(g1), id(g2))
print(g1.name,g2.name)

# class Singleton:
#     _instance = None
#
#     def __new__(cls, *args, **kwargs):
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#         return cls._instance
#
# class Game(Singleton):
#     def __init__(self, name):
#         if not hasattr(self, 'name'):  # Проверка на то, что атрибут еще не был установлен
#             self.name = name
#
# # Пример использования
# game1 = Game('Chess')
# game2 = Game('Checkers')
#
# print(game1.name)  # Вывод: Chess
# print(game2.name)  # Вывод: Chess
#
# print(game1 is game2)  # Вывод: True (оба экземпляра ссылаются на один и тот же объект)