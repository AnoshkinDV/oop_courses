class PhoneNumber:
    def __init__(self, number, fio):
        number = str(number)
        if len(number) == 11:
            self.number = int(number)
        if type(fio) is str:
            self.fio = fio


class PhoneBook:
    def __init__(self):
        self.spisok_number = []

    def add_phone(self, phone):
        self.spisok_number.append(phone)

    def remove_phone(self, indx):
        self.spisok_number.pop(indx)

    def get_phone_list(self):
        # sps = []
        # for numbers in self.spisok_number:
        #     sps.append(numbers.number)
        # return sps
        return self.spisok_number

p = PhoneBook()
p.add_phone(PhoneNumber(12345678901,'Сергей Балакирев'))
p.add_phone(PhoneNumber(12345678901,'Панда'))
phones = p.get_phone_list()
print(phones)
p.remove_phone(1)
phones = p.get_phone_list()
print(phones)

