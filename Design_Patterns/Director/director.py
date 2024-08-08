class Director:
    def __init__(self,strategy):
        self.strategy = strategy
        self.builder = None

    def set_builder(self, builder):
        self.builder = builder

    def construct_pizza(self):
        self.strategy.prepare_pizza(self.builder)
        return self.builder.get_pizza()

    def show_strategy_name(self):
        print('Strategy name:', self.strategy.name())