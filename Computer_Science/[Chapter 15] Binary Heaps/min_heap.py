# Write a function that takes a binary tree as a parameter and returns
# True if it is a minimal heap and False if it is not.
class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def min_heap(node):
    if node is None:
        return True

    if (node.left is not None and node.left.key < node.key) or (node.right is not None and node.right.key < node.key):
        return False
    return min_heap(node.left) and min_heap(node.right)
