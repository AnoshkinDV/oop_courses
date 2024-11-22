class StackObj:
    def __init__(self, data):
        self.__data = data
        self.__next = None

    @property
    def data(self):
        return self.__data

    @data.setter
    def data(self, value):
        self.__data = value

    @property
    def next(self):
        return self.__next

    @next.setter
    def next(self, obj):
        if isinstance(obj, StackObj) or obj is None:
            self.__next = obj


class Stack:
    def __init__(self):
        self.top = None
        self.last = None

    def push(self, obj):  # Это я сделал сам
        if self.last:
            self.last.next = obj
        self.last = obj
        if self.top is None:
            self.top = obj

    def pop(self):
        node = self.top
        while node.next != self.last:
            node = node.next  # node предпоследний
        self.last = node
        node.next = None
        return self.last

    def get_data(self):
        sps = []
        h = self.top
        while h:
            sps.append(h.data)
            h = h.next
        return sps


st = Stack()
st.push(StackObj('obj1'))
st.push(StackObj('obj2'))
st.push(StackObj('obj3'))
s = st.pop()
print(s)
st.pop()
res = st.get_data()
print(res)
