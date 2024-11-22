class Graph:
    def __init__(self,data,is_show=True):
        self.data=data[:] # нужно сделать копию списка, чтобы у каждого обьект был свой список
        self.is_show=is_show

    def set_data(self,data):
        self.data = data

    def show_table(self):
        if self.is_show:
            print(*self.data)
        else:
            print('Отображение данных закрыто')

    def show_graph(self):
        if self.is_show:
            print('Графическое отображение данных:', *self.data)
        else:
            print('Отображение данных закрыто')

    def show_bar(self):
        if self.is_show:
            print('Столбчатая диаграмм:', *self.data)
        else:
            print('Отображение данных закрыто')

    def set_show(self,fl_show):
        self.is_show=fl_show

#data_graph=list(map(int,input().split()))
gr1=Graph([1,3,4,5])
gr1.show_table()
gr1.show_bar()
gr1.set_show(False)
gr1.show_bar()
gr2=Graph([1,1,1,1,1])
gr2.show_table()
gr3=Graph([2,2,2,2])
gr3.show_table()
gr3.set_show(False)
gr3.show_graph()
gr3.set_show(True)
gr3.show_graph()


