import sys


class StreamData:
    def create(self, fields, lst_values):

        if len(fields) != len(lst_values):
            return False

        for i, key in enumerate(fields):
            setattr(self, key, lst_values[i]) # cоздает локальные атрибуты для экземпляра класса

        return True


class StreamReader:
    FIELDS = ('id', 'title', 'pages')

    def readlines(self):
        lst_in = list(map(str.strip, sys.stdin.readlines()))
        print(lst_in)
        sd = StreamData()
        res = sd.create(self.FIELDS, lst_in)
        print(sd)
        print(res)
        return sd, res

sr = StreamReader()
data, result = sr.readlines()
