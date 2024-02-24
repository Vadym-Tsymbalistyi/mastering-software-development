from unittest import TestCase, main
from binary_trees import BinaryTree, Node, insert_tree


class TestBinaryTree(TestCase):
    def setUp(self):
        self.tree = BinaryTree(1)
        self.tree.insert_left(2)
        self.tree.insert_right(3)

    def test_hes_left_nodes(self):
        self.assertTrue(self.tree.has_leaf_nodes())
        self.tree.left_child.insert_left(4)
        self.assertTrue(self.tree.has_leaf_nodes())
        self.assertFalse(self.tree.right_child.has_left_nodes())

    def test_insert_left(self):
        self.assertEqual(self.tree.left_child.key, 2)

    def test_insert_right(self):
        self.assertEqual(self.tree.right_child.key, 3)


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


if __name__ == '__main__':
    main()
