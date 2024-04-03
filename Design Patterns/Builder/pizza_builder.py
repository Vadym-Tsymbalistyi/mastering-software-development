class Director:
    def __init__(self):
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def constructor_pizza(self):
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
        self.pizza.add_dough = 'Middle dough'

    def add_filling(self):
        self.pizza.add_filling = ['Salami', 'Tomatoes', 'Cheese']


class Pizza:  #TO DO:
    pass
