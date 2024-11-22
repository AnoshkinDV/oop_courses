# print("Куда ты скачешь, гордый конь,")
# print("И где опустишь ты копыта?")
# print("О мощный властелин судьбы!")
# e = ZeroDivisionError('Деление на ноль')
# raise e
# print("Не так ли ты над самой бездной")
# print("На высоте, уздой железной")
# print("Россию поднял на дыбы?")
class ExceptionPrint(Exception):
    """Общий класс исключения принтера"""
class ExceptionPrintSendData(ExceptionPrint):
    """
    Класс исключения при отправке данных принтеру
    """
    def __init__(self,*args):
        self.message = args[0] if args else None
    def __str__(self):
        return f'Ошибка:{self.message}'

class PrintData:
    def print(self, data):
        self.send_data(data)
        print(f'печать:{str(data)}')

    def send_data(self,data):
        if not self.send_to_print(data):
            raise ExceptionPrintSendData

    def send_to_print(self,data):
        return False

p = PrintData()
# p.print('123')
try:
    p.print('123')
except ExceptionPrintSendData:
    print('Принтер не отвечает')
except ExceptionPrint:
    print('Общая ошибка печати')