# Реализуйте очередь с помощью двух стеков, чтобы временн я сложность
# постановки в очередь была равна О(1).
class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, item):  # константное время O(1),
        self.__s1.append(item)

    def dequeue(self):  # амортизированное время O(1)
        if not self.__s1 and not self.__s2:
            raise Exception("Cannot pop from empty queue")
        if not self.__s2:
            while self.__s1:
                self.__s2.append(self.__s1.pop())

        return self.__s2.pop()
