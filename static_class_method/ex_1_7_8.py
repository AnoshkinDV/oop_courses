from string import ascii_lowercase, digits


class CardCheck:
    CHARS_FOR_NAME = ascii_lowercase.upper() + digits + ' '

    @classmethod
    def check_card_number(cls, number):
        if type(number) != str:
            return False
        s = number.split('-')
        if len(s) != 4:
            return False
        for i in s:
            if len(i) != 4:
                return False
            if not i.isnumeric():
                return False
        return True


    @classmethod
    def check_name(cls, name):
        if all(char in cls.CHARS_FOR_NAME for char in name) and len(name.split()) == 2:
            return True
        else:
            return False


is_number = CardCheck.check_card_number('1234-1334-1144-1214-19191')
is_name = CardCheck.check_name('SERGEY BALAKIREV FNFN')
print(is_number)
print(is_name)

# def filter (s):
#     if len(s) != 4:
#         return False
#     for i in s:
#         if len(i) != 4:
#             return False
#         if not i.isnumeric():
#             return False
#     return True
#
#
# s = '1234-1234-1234-1234'
# print(filter(s.split('-')))
