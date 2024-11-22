class TreeObj:
    def __init__(self, indx, value=None):
        self.indx = indx
        self.value = value
        self.__left = None
        self.__right = None

    @property
    def left(self):
        return self.__left
    @left.setter
    def left(self,obj):
        self.__left = obj

    @property
    def right(self):
        return self.__right

    @right.setter
    def right(self, obj):
        self.__right = obj

class DecisionTree:
    @classmethod
    # Этот метод добавляет новый объект в бинарное дерево, добавляемы объект это obj, node это та вершина к которой объект добавляется
    def add_obj(cls,obj,node = None,left = True):
        # if node is None:
        #     cls.node = obj
        #     return cls.node
        if node: # если добавляем не корневой объект, то есть у нас уже есть корневая вершина не равная None
            if left:
                node.left = obj # Обратиться к объекту свойству left объекта node и присвоить ему значение obj, это работает в соответствии с setter
            else: #либо обращаемся к объекту свойству right объекта node(предыдущая вершина)
                node.right = obj
        return obj # Просто возвращаем добавленную вершину


    @classmethod
    def predict(cls,root,x): # root это указатель на корень дерева, то есть на самый первый объект Любит Python с индексом 0
            obj = root # Создадим вспомогательную переменную, то есть у нас obj and root будут ссылаться на один корневой объект
            while obj: # то есть мы будем перебирать объекты решающего дерева пока obj не равен None
                obj_next = cls.get_next(obj,x) # Сформируем переменную obj_next которая будет ссылаться на следующий объект решающего дерева
                if obj_next is None:
                    break
                obj  =  obj_next
                # Те мы будем проходить иерархически по решающему дереву до тех пор пока не дойдем до его листовой вершины, а листовая вершина это та которая ссылается на None
            return obj.value # Возвращаем значение листовой вершина, а это листовая вершина ссылается на None

    @classmethod
    def get_next(cls,obj,x):
        if x[obj.indx] == 1:
            return obj.left # Вернуть то что на что ссылается левая ветвь текущего объекта
        return obj.right

root = DecisionTree.add_obj(TreeObj(0))
v11 = DecisionTree.add_obj(TreeObj(1),root) #Добавляем вершину слева от корневой
v12 = DecisionTree.add_obj(TreeObj(2),root,False) #Добавляем вершину справа от корневой, тут прописываем False
DecisionTree.add_obj(TreeObj(-1,'будет программистом'),v11)
DecisionTree.add_obj(TreeObj(-1,'будет кодером'),v11,False)
DecisionTree.add_obj(TreeObj(-1,'не все потеряно'),v12)
DecisionTree.add_obj(TreeObj(-1,'безнадежен'),v12,False)
x = [1,1,0]
res = DecisionTree.predict(root,x)
print(res)