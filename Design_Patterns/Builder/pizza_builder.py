from Design_Patterns.Director.director import Director
from Design_Patterns.Strategy.strategy import DoughFirstStrategy, FillingFirstStrategy
from abc import ABC, abstractmethod


class PizzaBuilder(ABC):
    def __init__(self):
        self.pizza = Pizza()

    @abstractmethod
    def add_dough(self):
        pass

    @abstractmethod
    def add_filling(self):
        pass


    def get_pizza(self):
        return self.pizza


class SalamiPizzaBuilder(PizzaBuilder):
    def add_dough(self):
        self.pizza.dough = 'Middle dough'


    def add_filling(self):
        self.pizza.filling = ['Salami', 'Tomatoes', 'Cheese']



class Pizza:
    def __init__(self):
        self.dough = None
        self.filling = []

    def result(self):
        print('Pizza dough:', self.dough)
        print("Filling:", ",".join(self.filling))


director = Director(FillingFirstStrategy())
builder = SalamiPizzaBuilder()
director.set_builder(builder)
pizza = director.construct_pizza()
director.show_strategy_name()
print('Pizza salami:')
pizza.result()

director = Director(DoughFirstStrategy())
builder = SalamiPizzaBuilder()
director.set_builder(builder)
pizza = director.construct_pizza()
director.show_strategy_name()
pizza.result()
