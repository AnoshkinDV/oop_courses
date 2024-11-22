class Geom:
    __name = 'Geom'
    def __init__(self,x1,y1,x2,y2):
        print(f'инициализатор Geom для {self.__class__}')
        self._x1 = x1
        self._y1 = y1
        self._x2 = x2
        self._y2 = y2
        self._name = self.__name

    def __verify_coord(self,coord):
        return 0 <= coord <=100

#Добавим еще один дочерний класс Rect
class Rect(Geom):
    def __init__(self,x1,y1,x2,y2,fill = 'red'):
        super().__init__(x1,y1,x2,y2)
        print('инициализатор Rect')
        self.__verify_coord(x1)
        self._fill = fill
    def draw(self): # Это переопределение метода draw
        print("Рисование прямоугольника")

    def get_coords(self):
        return (self._x1, self._y1)



r = Rect(0,0,10,20)
print(r._name)
#{'_Geom__x1': 0, '_Geom__y1': 0, '_Geom__x2': 10, '_Geom__y2': 20, '_Rect__fill': 'red'}
print(r.__dict__)