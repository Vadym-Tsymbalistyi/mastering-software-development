from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def pizza_strategy(self, pizza):
        pass

    def name(self):
        pass


class FillingFirstStrategy(Strategy):
    def pizza_strategy(self, pizza):
        return pizza.filling + [pizza.dough]

    def name(self):
        return 'FillingFirstStrategy'


class DoughFirstStrategy(Strategy):
    def pizza_strategy(self, pizza):
        return [pizza.dough] + pizza.filling

    def name(self):
        return 'DoughFirstStrategy'
