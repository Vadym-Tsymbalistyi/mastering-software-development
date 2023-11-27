from unittest import TestCase, main
from Chapter_10_Linked_Lists import Node, LinkedList


class TestLinkedList(TestCase):
    def setUp(self):
        self.node1 = Node(1, "A")
        self.linked_list = LinkedList(self.node1)
        self.linked_list.append(1, "Data1")
        self.linked_list.append(2, "Data2")
        self.linked_list.append(3, "Data3")

    def test_append(self):
        # Test the append method
        self.linked_list.append(4, "Data4")
        self.assertEqual(self.linked_list.head.data, "A")
        self.assertEqual(self.linked_list.tail.data, "Data4")

    def test_print(self):
        # Test the print method
        self.linked_list.print()

        # self.assertEqual     ????

    def test_find_node_by_id(self):
        # Test the find_node_by_id method
        node = self.linked_list.find_node_by_id(2)
        self.assertEqual(node.data, "Data2")

    def test_detect_cycle_without_cycle(self):
        self.assertFalse(self.linked_list.detect_cycle())

    def test_detect_cycle_with_cycle(self):
        self.linked_list.create_cycle(3, 1)
        self.assertTrue(self.linked_list.detect_cycle_ring())  # ring cycle

        self.linked_list.create_cycle(3, 2)
        self.assertTrue(self.linked_list.detect_cycle_loop())  # loop cycle


if __name__ == '__main__':
    main()
