class Table:
    def __init__(self, model, color):
        self.set_model_and_color(model, color)

    def set_model_and_color(self, model, color):
        self.model = model
        self.color = color

class RoundTable(Table):
    def __init__(self, model, color, radius, height):
        super().__init__(model, color)
        self.radius = radius
        self.height = height

    def set_params(self, model, color, radius, height):
        self.model = model
        self.color = color
        self.radius = radius
        self.height = height

rt = RoundTable('PC', 'brown', 500, 750)
tb = Table('Home', 'white')

color = rt.color
rt.set_params('Home','red',700,1000)
rt.set_model_and_color('Home','red')
tb.set_params()
#AttributeError: 'Table' object has no attribute 'set_params'
h = tb.model
print(h)
m = tb.height
#AttributeError: 'Table' object has no attribute 'height'