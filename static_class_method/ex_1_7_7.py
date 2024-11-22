from string import ascii_lowercase, digits


class FormLogin:
    def __init__(self, lgn, psw):
        self.login = lgn
        self.password = psw

    def render_template(self):
        return "\n".join(['<form action="#">', self.login.get_html(), self.password.get_html(), '</form>'])


class TextInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits

    @classmethod
    def check_name(cls, name):
        if type(name) != str or not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        if not all(char in cls.CHARS_CORRECT for char in name):
            raise ValueError("некорректное поле name")
        # cls.name = name

    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='login'>{self.name}: <input type ='text' size=<{self.size} />"


class PasswordInput:
    CHARS = "абвгдеёжзийклмнопрстуфхцчшщьыъэюя " + ascii_lowercase
    CHARS_CORRECT = CHARS + CHARS.upper() + digits
    def check_name(cls, name):
        if type(name) != str or not 3 <= len(name) <= 50:
            raise ValueError("некорректное поле name")
        if not all(char in cls.CHARS_CORRECT for char in name):
            raise ValueError("некорректное поле name")
        # cls.name = name
    def __init__(self, name, size=10):
        self.check_name(name)
        self.name = name
        self.size = size

    def get_html(self):
        return f"<p class='passwod'>{self.name}: <input type ='text' size=<{self.size} />"


login = FormLogin(TextInput('ffjfjfjfj'), PasswordInput("Пароль"))
html = login.render_template()
print(login)
print(html)
