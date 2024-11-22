class Point:
    # def __new__(cls, *args, **kwargs):
    #     copy = super().__new__(cls)
    #     return copy
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def clone(self):
        return Point(self.x,self.y)


pt = Point(1,2)
pt_clone = Point.clone(pt)
print(pt)
print(pt_clone)
# Сделано , но забыл return


