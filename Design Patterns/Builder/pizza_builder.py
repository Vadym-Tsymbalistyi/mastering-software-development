class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.builder.make_pizza()
        self.builder.add_dough()
        self.builder.add_filling()


class PizzaBuilder:
    def __init__(self):
        self.pizza = None

    def make_pizza(self):
        self.pizza = Pizza()

    def add_dough(self):
        pass

    def add_filling(self):
        pass


class SalamiPizzaBuilder(PizzaBuilder):

    def add_dough(self):
        self.pizza.dough = 'Middle dough'

    def add_filling(self):
        self.pizza.filling = ['Salami', 'Tomatoes', 'Cheese']


class Pizza:  # TO DO:
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
