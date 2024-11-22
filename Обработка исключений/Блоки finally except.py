# try:
#     f = open('myfile2.txt')
# except FileNotFoundError:
#     print('Невозможно открыть файл')

# try:
#     x, y = map(int, input().split())
#     res = x / y
# except ZeroDivisionError as z: # Переменная z является ссылкой на экземпляр класса исключения ZeroDivisionError
#     print(z)
# except ValueError as z:
#     print(z) # Выдает стандартное сообщение которое заложено в классе ValueError
# # else:
# #     print('Исключение не произошло')
# finally:
#     print('Выполняется всегда') # Выполняется всегда вне зависимости произошли ли ошибки в блоке try


# пример того когда нам нужен блок finally -  это работа с файлами

# try:
#     f = open('myfile.txt')
#     f.write('Hello') # Ошибка произошла в этой строчке!!!
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Другое исключение')
# finally:
#     if f:
#         f.close()
#         print('Файл закрыли')

# Но такие грамоздские конструкции редко используют на практике обычно, используют файловый менеджер
# try:
#     with open('myfile.txt') as f:
#         f.write('Hello')
# except FileNotFoundError as z:
#     print(z)
# except:
#     print('Другая ошибка')

# def get_values():
#     try:
#         x,y = map(int,input().split())
#         return x, y
#     except ValueError as z:
#         print(z) # Здесь выводим сообщение которое заложено в этом исключении
#         #Если были введены кривые значения то возвращается кортеж в виде нулей
#         return 0,0
#     finally:
#         print('Выполняется до return')
#
# x,y = get_values()
# print(x,y)

# Также можно использовать вложенные блоки try except


# try:
#     x,y = map(int,input().split())
#     try:
#         res = x/y
#     except ZeroDivisionError as z:
#         print(z)
#
# except ValueError as z:
#     print(z) # Здесь выводим сообщение которое заложено в этом исключении

def div(x,y):
    try:
        return x/y
    except ZeroDivisionError:
        return 'Деление на ноль'
res = 0
try:
    x, y  = map(int,input().split())
    res = div(x, y)
except ValueError as z:
    print(z)

print(res)

