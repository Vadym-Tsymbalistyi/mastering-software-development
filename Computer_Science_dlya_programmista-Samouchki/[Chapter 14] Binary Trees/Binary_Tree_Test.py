from unittest import TestCase, main
from Chapter_14_Binary_Trees import BinaryTree, Node, insert_tree


class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree(1)
        self.tree.insert_left(2)
        self.tree.insert_right(3)
        self.tree.left_child.insert_left(4)
        self.tree.right_child.insert_right(5)

    def test_hes_left_nodes(self):
        self.assertTrue(self.tree.has_leaf_nodes())
        self.assertTrue(self.tree.left_child.has_leaf_nodes())

    def test_insert_left(self):
        new_value = 6
        self.tree.left_child.insert_left(new_value)
        self.assertEqual(self.tree.left_child.left_child.key, new_value)

    def test_insert_right(self):
        new_value = 7
        self.tree.right_child.insert_right(new_value)
        self.assertEqual(self.tree.right_child.right_child.key, new_value)




class TestNode(TestCase):

    def setUp(self):
        self.tree = Node(1)
        self.tree.left = Node(2)
        self.tree.right = Node(3)
        self.tree.left.left = Node(4)
        self.tree.right.right = Node(5)

    def test_insert_tree(self):
        insert_tree(self.tree)

        self.assertEqual(self.tree.key, 1)
        self.assertEqual(self.tree.left.key, 3)
        self.assertEqual(self.tree.right.key, 2)

    # def test_print_tree(self):


if __name__ == '__main__':
    main()
