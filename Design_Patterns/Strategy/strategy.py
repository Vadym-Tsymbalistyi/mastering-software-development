from abc import ABC, abstractmethod


class Strategy(ABC):
    @abstractmethod
    def pizza_strategy(self, pizza):
        pass

class FillingFirstStrategy(Strategy):
    def pizza_strategy(self, pizza):
        return pizza.filling + [pizza.dough]

class DoughFirstStrategy(Strategy):
    def pizza_strategy(self, pizza):
        return [pizza.dough] + pizza.filling
