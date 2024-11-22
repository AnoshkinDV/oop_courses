class WindowsDlg:
    def __init__(self, title = None, width = None, height = None):
        if not type(title) is str:
            raise TypeError('Неккоректное значение названия заголовка')
        self.__title = title
        if not type(width) is int:
            raise TypeError('Неккоректное значение ширины окна')
        self.__width = width
        if not type(height) is int:
            raise TypeError('Неккоректное значение высоты окна')
        self.__height = height

    def show(self):
        print(f'{self.__title}:{self.__width},{self.__height}')

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) is int and 0 <= value <= 10000:
            self.__width = value
            self.show()

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) is int and 0 <= value <= 10000:
            self.__width = value
            self.show()

w = WindowsDlg('Диалог1',100,10)
w.width = -120
