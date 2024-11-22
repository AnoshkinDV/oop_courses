#Самое сложное это догадаться до того как хранить эти связки, лучший вариант это связки

class Translator:
    def add(self, eng, rus):
        if 'tr' not in self.__dict__:
            self.tr = {} # tr будет являться локальным атрибутом экземпляра класса, то есть объекта класса Translator

        self.tr.setdefault(eng,[])  # с каждым английским словом будет связан список и в этом списке будут храниться русские слова
        if rus not in self.tr[eng]:
            self.tr[eng].append(rus)
# если в словаре такого нет ключа, то создаем пустой список, то есть с каждым английским словом у нас будет связан список, а если ключ уже есть то ничего не происхолит
    def remove(self, eng):
        # try:
        #     self.tr.pop(eng)  # удаляет значения их словаря которое связано с соответствующим ключом, по дефолту если нет таког ключа то ничего не выдаст в ответ, но можно узать
        # except KeyError:
        #     print('Такого ключа нет')
        del self.tr[eng]
    def translate(self, eng):
        return self.tr[eng]

tr = Translator()
tr.add('tree','дерево')
tr.add('car','машина')
tr.add('car','автомобиль')
tr.add('leaf','лист')
tr.add('river','река')
tr.add('milk','молоко')

tr.add('go','идти')
tr.add('go','ехать')
tr.add('go','ходить')

print(*tr.translate('go'))


