TYPE_OS = 2
class DialogWindows:
    name_class = 'DialogWindows'

class DialogLinux:
    name_class = 'DialogLinux'

class Dialog:
    def __new__(cls, *args, **kwargs):  # контролирует процесс создания объектов класса
        if TYPE_OS == 1:  # если атрибут инстанс принимает значение None то тогда мы в этой строчке создаем новый экземпляр класа
            return super().__new__(DialogWindows)
        else:
            return super().__new__(DialogLinux)

    def __init__(self, name):
        self.name = name

dlg = Dialog('Windows')
print(dlg)
