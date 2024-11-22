# Здесь объявляется класс Factory

class Loader:
    @classmethod
    def parse_format(cls,string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    @staticmethod
    def build_sequence():
        return []
    @staticmethod
    def build_number(string):
        return float(string)



# s = input()
res = Loader.parse_format('2,10,-5', Factory)
print(res)
