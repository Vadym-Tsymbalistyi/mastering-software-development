from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def prepare_pizza(self, builder):
        pass

    def name(self):
        pass


class FillingFirstStrategy(Strategy):
    def prepare_pizza(self, builder):
        builder.add_filling()
        builder.add_dough()


    def name(self):
        return 'FillingFirstStrategy'


class DoughFirstStrategy(Strategy):
    def prepare_pizza(self, builder):
        builder.add_dough()
        builder.add_filling()
    def name(self):
        return 'DoughFirstStrategy'
