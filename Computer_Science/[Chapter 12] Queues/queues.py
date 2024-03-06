# Implement the queue using two stacks so that the time complexity of queuing is equal to O(1).
class Queue:
    def __init__(self):
        self.__s1 = []
        self.__s2 = []

    def enqueue(self, item):  # constant time O(1),
        self.__s1.append(item)

    def dequeue(self):  # amortized time O(1)
        if not self.__s1 and not self.__s2:
            raise Exception("Cannot pop from empty queue")
        if not self.__s2:
            while self.__s1:
                self.__s2.append(self.__s1.pop())

        return self.__s2.pop()
