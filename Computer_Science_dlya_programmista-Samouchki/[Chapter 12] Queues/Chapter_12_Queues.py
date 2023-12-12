# Реализуйте очередь с помощью двух стеков, чтобы временн я сложность
# постановки в очередь была равна О(1).
class Queue():
    def __init__(self):
        self.s1 = []
        self.s2 = []

    def enqueue(self, item):  # константное время O(1),
        self.s1.append(item)

    def dequeue(self):  # амортизированное время O(1)
        if not self.s2:
            while self.s1:
                self.s2.append(self.s1.pop())

        if not self.s2:
            raise Exception("Cannot pop from empty queue")

        return self.s2.pop()


queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())
print(queue.dequeue())
print(queue.dequeue())
