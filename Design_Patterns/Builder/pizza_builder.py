from Design_Patterns.Director.director import Director
from Design_Patterns.Strategy.strategy import DoughFirstStrategy, FillingFirstStrategy
from abc import ABC, abstractmethod


class PizzaBuilder(ABC):
    @abstractmethod
    def build(self):
        return self

    @abstractmethod
    def add_dough(self):
        return self

    @abstractmethod
    def add_filling(self):
        return self


class SalamiPizzaBuilder(PizzaBuilder):
    def __init__(self, strategy):
        self.pizza = Pizza(strategy)

    def add_dough(self):
        self.pizza.dough = 'Middle dough'
        return self

    def add_filling(self):
        self.pizza.filling = ['Salami', 'Tomatoes', 'Cheese']
        return self

    def build(self):
        return self.pizza


class Pizza:
    def __init__(self, strategy):
        self.dough = None
        self.filling = []
        self.strategy = strategy

    def result(self):
        print('Name strategy:', self.strategy.name())
        print('Pizza strategy:', self.strategy.pizza_strategy(self))
        print('Pizza dough:', self.dough)
        print("Filling:", ",".join(self.filling))


director = Director()
builder = SalamiPizzaBuilder(FillingFirstStrategy())
director.set_builder(builder)
director.construct_pizza()
pizza = builder.build()
print('Pizza salami:')
pizza.result()

builder = SalamiPizzaBuilder(DoughFirstStrategy())
director.set_builder(builder)
director.construct_pizza()
pizza = builder.build()
pizza.result()
