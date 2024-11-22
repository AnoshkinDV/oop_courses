class Clock:
    def __init__(self,tm):
        self.__time = 0 #Приватно локальное свойство
        if self.__check_time(tm):
            self.__time = tm


    def set_time(self, tm):
        if self.__check_time(tm):
            self.__time = tm
    @classmethod
    def __check_time(cls, tm): # Приватный метод класса
        # if type(tm) is int and 0 <= tm < 100000:
        #     return True
        # else:
        #     return False
        return type(tm) is int and 0 <= tm < 100000
    def get_time(self):
        return self.__time

clock = Clock(3445)
print(clock.get_time())