# Реализуйте очередь с помощью двух стеков, чтобы временн я сложность
# постановки в очередь была равна О(1).
class Queue:
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):  # константное время O(1),
        self.s1.append(item)

    def dequeue(self):  # амортизированное время O(1)
        if not self.s1 and not self.s2:
            raise Exception("Cannot pop from empty queue")
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        return self.s2.pop()
