#Это методы экземпляра класса AppStore, тк вызывается store = AppStore(),store.add_application(app_youtube), то есть здесь не нужны классметоды

class Application:
    def __init__(self, name):
        self.name = name
        self.blocked = False


class AppStore:
    def __init__(self):
        self.sps = []

    def add_application(self, app):
        self.sps.append(app)

    def remove_application(self, app):
        self.sps.remove(app)

    def block_application(self,app):
        if app in self.sps:
            app.blocked = True

    def total_apps(self):
        return len(self.sps)

store = AppStore()
app_youtube = Application('YouTUbe')
store.add_application(app_youtube)
app_google = Application('Google')
store.add_application(app_google)
app_yandex = Application('Yandex')
# store.block_application(app)
store.remove_application(app_youtube)
print(store.total_apps())
