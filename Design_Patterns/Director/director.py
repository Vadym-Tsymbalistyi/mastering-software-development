from Design_Patterns.Observer.observer import Subject


class Director(Subject):
    def __init__(self, strategy):
        super().__init__()
        self.strategy = strategy
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.strategy.prepare_pizza(self.builder)
        pizza = self.builder.get_pizza()
        self.notify()
        return pizza

    def show_strategy_name(self):
        print('Strategy name:', self.strategy.name())
