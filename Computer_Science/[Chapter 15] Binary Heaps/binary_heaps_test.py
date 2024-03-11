from unittest import TestCase, main
from min_heap import BinaryTree, min_heap


class TestBinaryTree(TestCase):
    def test_min_heaps_true(self):
        self.root = BinaryTree(2)
        self.root.left = BinaryTree(3)
        self.root.right = BinaryTree(4)
        self.root.left.left = BinaryTree(5)
        self.root.right.right = BinaryTree(6)
        self.result = min_heap(self.root)
        self.assertTrue(self.result)

    def test_min_heaps_false(self):
        self.root = BinaryTree(2)
        self.root.left = BinaryTree(3)
        self.root.right = BinaryTree(1)
        self.result = min_heap(self.root)
        self.assertFalse(self.result)

    def test_heaps_empty_tree(self):
        self.root = None
        self.result = min_heap(self.root)
        self.assertTrue(self.result)


if __name__ == '__main__':
    main()
