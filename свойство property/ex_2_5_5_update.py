class WindowsDlg:
    def __init__(self, title, width, height):
        self.__title = title
        self.__width,self.__height = None # Для локальных атрибутов делаем проверку, для начальных значений присваеваем None, None - когда еще ничего не присваивали
        self.__width = width # само присвоение сделаем через объекты свойства, так как в объектах свойства будет сделана проверка на корректность
        self.__height = height
    def show(self):
        print(f'{self.__title}:{self.__width},{self.__height}')

    @property
    def width(self): # объекты свойства
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int and 0 <= value <= 10000:
            if self.__width: # если это значние не равно None
                self.show()
            self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and 0 <= value <= 10000:
            if self.__height: # не None
                self.show()
            self.__height = value