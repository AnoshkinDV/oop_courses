# Это методы класса так все эти методы вызываеются через класс а не через экземпляр класса как было в прошлом подвиге
# Viber.add_message(msg)
# Viber.add_message(Message('Это курс по Python ООП.'))
# Viber.add_message(Message('Что вы о нем думаете?'))
# Viber.set_like(msg)
# Viber.remove_message(msg)
# Сами сообщения будут объекты другого класса
# Атрибутом класса Viber может быть список и провести можно те же самые операции (методы)
class Message:
    def __init__(self, text):
        self.text = text
        self.like = False


class WhatsApp:
    dict = {}

    @classmethod
    def add_message(cls, msg):
        cls.dict[id(msg)] = msg

    @classmethod
    def remove_message(cls, msg):
        key = id(msg)
        if key in cls.dict:
            cls.dict.pop(key)  # либо del dict[id(msg)]

    @classmethod
    def set_like(cls, msg):
        if msg.like:
            msg.like = False
        else:
            msg.like = True

    @classmethod
    def last_message(cls, num):
        for m in tuple(cls.dict.values())[-num:]: # взять отрицательный срез от значений словаря просто так нельзя
            print(m)

    @classmethod
    def total_message(cls):
        return len(cls.dict)


msg = Message('Всем привет!')
WhatsApp.add_message(msg)
WhatsApp.add_message(Message('Это курс по Python ООП.'))
WhatsApp.add_message(Message('Что вы о нем думаете?'))
WhatsApp.set_like(msg)
WhatsApp.remove_message(msg)
WhatsApp.last_message(2)
