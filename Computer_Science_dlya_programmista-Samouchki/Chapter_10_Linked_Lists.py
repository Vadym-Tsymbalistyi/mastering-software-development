# 1. Создайте связный список, содержащий числа от 1 до 100. Затем выведите
# каждый узел списка.

# 2. Создайте два связных списка: один содержащий цикл, а другой — без цикла.
# Убедитесь, что в каждом из них есть метод detect_cycle для определения
# того, имеется ли в списке цикл. Вызовите detect_cycle для обоих списков.

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __init__(self, node):
        self.head = node

    # head = None
    # head = Node(data = 1, next = None)
    # head = Node(data = 1, next = Node(2))

    # LinkedList {
    #            head = Node(data = 1, next = Node(2))
    #            tail = Node(data = 1, next = Node(2))
    #
    #
    #            Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> None
    # currentNode ^
    # }

    def append(self, data):
        current_node = Node(data)
        if self.head is None:
            self.head = current_node
            self.tail = current_node
        else:
            self.tail.next = current_node
            self.tail = current_node

    def print(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next

    def create_cycle(self, node_id_from, node_id_to):
        # TODO: implement
        return

    #
    # There is no Cycle: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> None
    # There is a Cycle Ring: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> Node(1, next = Node(2))
    # There is a Cycle Loop: Node(1, next = Node(2)) -> Node(2, next = Node(3)) -> Node(3, next = None) -> Node(2, next = Node(2))
    def detect_cycle(self): # should return  True or False
        # TODO: implement
       return detect_cycle_ring(self) + detect_cycle_loop(self) # pseudo code


    def detect_cycle_ring(self):  # should return  True or False
        return False #TODO: implement

    def detect_cycle_loop(self):  # should return  True or False
        visited_nodes = ...

        currentNode = self.head
        while currentNode.next is not None:
            if visited_nodes contains currentNode: # pseudo code
                return True
            visited_nodes.append(currentNode)
            currentNode = currentNode.next
        return False




linked_list = LinkedList()
for i in range(1, 101):
    linked_list.append(i)
linked_list.print()

