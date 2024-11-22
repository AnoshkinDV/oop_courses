from math import sqrt


class LineTo:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


class PathLines:
    def __init__(self, *args): # Произвольное число аргументов - объектов класса LineTo
        self.list_lines = [LineTo()]+list(args)

    def add_line(self, line):
        self.list_lines.append(line)

    def get_length(self):
        L = 0
        for i in range(1,len(self.list_lines)):
                L += sqrt((self.list_lines[i].x - self.list_lines[i-1].y) ** 2 + (self.list_lines[i].y - self.list_lines[i-1].y) ** 2)
        return L
        # return sqrt((self.list_lines[0].x)**2 + (self.list_lines[0].y)**2)
    def get_path(self):
        # if self.list_lines is None:
        #     return []
        return self.list_lines[1:]
p = PathLines(LineTo(10,20),LineTo(10,30))
p.add_line(LineTo(20,-10))
print(p.get_length())
res = p.get_path()
print(res)
# p = PathLines(LineTo(10,20))
# print(p.get_length())

