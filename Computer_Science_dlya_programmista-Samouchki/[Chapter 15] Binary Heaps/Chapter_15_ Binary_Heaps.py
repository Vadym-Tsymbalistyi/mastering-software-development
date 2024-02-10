#Напишите функцию, которая принимает двоичное дерево в качестве параме-
#тра и возвращает True, если это минимальная куча, и False, если нет.
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


root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.right.right = BinaryTree(5)
result = min_heap(root)
print(result)
