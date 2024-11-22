def func2():
    try:
        return 1/0
    except:
        print('func2 error')
def func1():
    try:
        return func2()
    except:
        print('func1 error')

print("Я к вам пишу – чего же боле?")
print("Что я могу еще сказать?")
print("Теперь, я знаю, в вашей воле")
func1()
print("Меня презреньем наказать.")
print("Но вы, к моей несчастной доле")
print("Хоть каплю жалости храня,")
print("Вы не оставите меня.")

# Видим стек распространения исключения
# File
# "C:\Users\79022\Desktop\selfedu_oop\Обработка исключений\Распространение исключений.py", line
# 6, in < module >
# func1()
# File
# "C:\Users\79022\Desktop\selfedu_oop\Обработка исключений\Распространение исключений.py", line
# 2, in func1

