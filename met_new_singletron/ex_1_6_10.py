# Здесь объявляется класс Factory

class Loader:
    def parse_format(self, string, factory):
        seq = factory.build_sequence()
        for sub in string.split(","):
            item = factory.build_number(sub)
            seq.append(item)

        return seq


class Factory:
    def build_sequence(self):
        self.sps = []
        return self.sps

    def build_number(self, string):
        return float(string)


# эти строчки не менять!
ld = Loader()
# s = input()
res = ld.parse_format('2,10,-5', Factory())
print(res)
