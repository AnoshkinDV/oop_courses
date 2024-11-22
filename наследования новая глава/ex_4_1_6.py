class GenericView:
    def __init__(self, methods=('GET',)):
        self.methods = methods

    def get(self, request):
        return ""

    def post(self, request):
        pass

    def put(self, request):
        pass

    def delete(self, request):
        pass


class DetalView(GenericView):
    def __init__(self, methods = ('GET',)):
        super().__init__(methods)
        self.request_dict = {}

    def render_request(self, request, method):
        if method.upper() not in self.methods:
            raise TypeError('Данный запрос не может быть выполнен')
        # return self.get(request)
        f = getattr(self,method.lower(),False)
        if f:
            return f(request)
        # return getattr(self,method,self.get)(request) # Вызывается необходимый метод, например get и он принимает параметр request - это словарь

    def get(self, request):
        if not type(request) is dict:
            raise TypeError('requst не является словарем')
        if 'url' not in request:
            raise ValueError("Ключ 'url' является обязательным")
        # for key, value in request.items():
        #     self.request_dict[key] = value
        print(f"url:<{request['url']}>")


dv = DetalView(('GET','POST'))
html = dv.render_request({'url':'https://site.ru/home'},'GET')
