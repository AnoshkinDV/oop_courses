import random
class Line:
    def __init__(self,a,b,c,d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a,b)
        self.ep = (c,d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)


elements = [(Line,Rect,Ellipse)[random.randint(0,2)](1,2,3,4) for n in range(217)]
for obj in elements:
    if isinstance(obj,Line): # ф-я для проверки является ли объект экземпляром опредленного класса, два аргумента: объект и класс(кортеж классов)
        obj.sp = obj.sp = 0,0






