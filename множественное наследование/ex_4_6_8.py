# class RetriveMixin:
#     def get(self, request):
#         return "GET: " + request.get('url')
#
#
# class CreateMixin:
#     def post(self, request):
#         return "POST: " + request.get('url')
#
#
# class UpdateMixin:
#     def put(self, request):
#         return "PUT: " + request.get('url')
#
#
# class GeneralView:
#     allowed_methods = ('GET','POST','PUT','DELETE')
#     def render_request(self,request):
#         method = request.get('method').upper()
#         if method not in self.allowed_methods:
#             raise TypeError(f"Метод {request.get('method')} не разрешен.")
#         method_request = self.__getattribute__(method.lower())
#         if method_request:
#             return method_request(request)
#
# class DetailView(RetriveMixin, UpdateMixin, GeneralView):
#     allowed_methods = ('GET', 'POST', )
#
# view = DetailView()
# html = view.render_request({'url': 'https://stepik.org/course/116336/', 'method': 'GET'})
# print(html)   # GET: https://stepik.org/course/116336/

# class A:
#     def __init__(self, name, old):
#         super().__init__()
#         self.name = name
#         self.old = old
#
# class B:
#     def __init__(self, *args, **kwargs):
#         super().__init__(*args, **kwargs)
#
# class C(B,A):
#     def __init__(self, name, old, weight, height):
#         super().__init__(name, old)
#         self.weight = weight
#         self.height = height
#
# person = C("Balakirev", 33, 80, 185)
# print(person.name)  # Вывод: Balakirev
# print(person.old)   # Вывод: 33
# print(person.weight)  # Вывод: 80
# print(person.height)  # Вывод: 185

import requests