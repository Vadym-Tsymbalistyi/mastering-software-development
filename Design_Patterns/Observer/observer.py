from abc import ABC, abstractmethod


class Observer(ABC):
    @abstractmethod
    def update(self, subject):
        pass


class Subject(ABC):
    def __init__(self):
        self.observers = []

    def attach(self, observer):
        self.observers.append(observer)
        pass

    def detach(self, observer):
        self.observers.remove(observer)
        pass

    def notify(self):
        for observer in self.observers:
            observer.update(self)
