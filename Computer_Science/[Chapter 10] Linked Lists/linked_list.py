# Create a linked list containing numbers from 1 to 100. Then output each node of the list.
# Create two linked lists, one containing a cycle and one without a cycle.
# Make sure that each list has a detect_cycle method to determine whether the list contains a cycle.
# Call detect_cycle on both lists.


class Node:
    def __init__(self, node_id, data):
        self.data = data
        self.next = None
        self.id = node_id

    def __str__(self):
        return f"""node ID: {self.id}, data = {self.data}"""


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __init__(self, node: Node):
        self.head = node
        self.tail = node

    def append(self, node_id, data):
        current_node = Node(node_id, data)
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
        from_node = self.find_node_by_id(node_id_from)
        to_node = self.find_node_by_id(node_id_to)

        if from_node is not None and to_node is not None:
            from_node.next = to_node
            print("Cycle  created.")
            return True
        else:
            print("Warning: Cycle not created.")
            return False

    def find_node_by_id(self, node_id):
        current_node = self.head
        while current_node is not None:
            if current_node.id == node_id:
                return current_node
            current_node = current_node.next
        return None

    def detect_cycle(self):
        return self.detect_cycle_ring() or self.detect_cycle_loop()

    # O(N/2)
    def detect_cycle_ring(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow is fast:
                return True
        return False

    # O(N*logN)
    def detect_cycle_loop(self):
        visited_nodes = dict()
        currentNode = self.head
        while currentNode.next is not None:
            if currentNode in visited_nodes:
                return True
            visited_nodes[currentNode] = True
            currentNode = currentNode.next
        return False
