# 1. Создайте связный список, содержащий числа от 1 до 100. Затем выведите
# каждый узел списка.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def print(self):
        node = self.head
        while node is not None:
            print(node.data)
            node = node.next


linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)
linked_list.print()


# 2. Создайте два связных списка: один содержащий цикл, а другой — без цикла.
# Убедитесь, что в каждом из них есть метод detect_cycle для определения
# того, имеется ли в списке цикл. Вызовите detect_cycle для обоих списков.
class Node:
    def __init__(self, data, next=None):
        self.data = data
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = Node(data)

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end='->')
            node = node.next
        print('None')

    def detect_cycle(self):
        slow = self.head
        fast = self.head
        while True:
            try:
                slow = slow.next
                fast = fast.next.next
                if slow is fast:
                    return True
            except:
                return False


linked_list = LinkedList()
linked_list.append(1)
linked_list.append(2)
linked_list.print()

linked_list2 = LinkedList()
linked_list2.append(1)
linked_list2.append(2)
linked_list2.detect_cycle()
