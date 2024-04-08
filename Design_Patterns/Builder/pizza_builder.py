from Design_Patterns.Director.director import Director


class PizzaBuilder:
    def __init__(self):
        self.pizza = Pizza()

    def build(self):
        return self.pizza

    def add_dough(self):
        return self

    def add_filling(self):
        return self


class SalamiPizzaBuilder(PizzaBuilder):

    def add_dough(self):
        self.pizza.dough = 'Middle dough'
        return self

    def add_filling(self):
        self.pizza.filling = ['Salami', 'Tomatoes', 'Cheese']
        return self


class Pizza:
    def __init__(self):
        self.dough = None
        self.filling = []

    def result(self):
        print('Pizza dough:', self.dough)
        print("FilLing:", ",".join(self.filling))


director = Director()
builder = SalamiPizzaBuilder()
director.set_builder(builder)
director.construct_pizza()
pizza = builder.pizza
print('Pizza salami')
pizza.result()
