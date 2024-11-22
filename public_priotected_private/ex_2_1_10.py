from random import randint as rnd, choice as ch
from string import ascii_lowercase, digits, ascii_uppercase
from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()
class EmailValidator:
    EMAIL_CHARS = ascii_lowercase + ascii_uppercase + digits + '_.@'  # латинские символы цифры
    MAIL = ascii_lowercase + ascii_uppercase + digits + '_'

    def __new__(cls, *args,
                **kwargs):  # Это для того чтобы еблан не создавал объекты класса, так как нам интересны методы класса, то есть в new просходит создание экземпялров, а мы ставим запрет
        return None

    @classmethod
    # ВСЕ МЕТОДЫ МЫ ВЫЗЫВАЕМ ЧЕРЕЗ КЛАСС
    def check_mail(cls, email): # метод который работает с АТРИБУТАМИ КЛАССА(EMAIL_CHARS,MAIL, статическая ф-я def __is_email_str(email))  а не локальными атрибутами Экземпляра, здесь они впринципе не участвуют по заданию
        if not cls.__is_email_str(email):  # Если этот метод возвратит False, то возвращаем и в check_false тожe False при помощи инверсии
            return False  # not False это Тру переходим внутрь
        # if not set(email) < set(cls.EMAIL_CHARS):  # Если в email входят недопустимые символы
        #     return False

        for x in email:
            if x not in cls.EMAIL_CHARS:
                return False
        s = email.split('@')
        # print(s)
        if email.count('@') != 1:
            return False
        # if len(s) != 2:  # если длина s не равна двум или  собачек вообще нет, то False
        #     return False
        if len(s[0]) > 100 or len(s[1]) > 50:
            return False
        if '.' not in s[1]:
            return False
        if '..' in email:
            return False
        return True

    @classmethod
    def get_random(cls):
        return ''.join(ch(cls.MAIL) for _ in range(0, rnd(1, 100))) + '@gmail.com'

    @staticmethod
    def __is_email_str(email): # Здесь у нас статик метод который принимает только аргументы и плюс он приватный то есть работает только внутри класса
        return type(email) is str

m = EmailValidator()
print(m)
print(EmailValidator.check_mail(EmailValidator.get_random()))
print(EmailValidator.check_mail('sc____lib@list.ru'))
print(EmailValidator.get_random())
