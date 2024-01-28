# 1. Добавьте в код вашего двоичного дерева метод под названием has_leaf_nodes.
# Метод должен вернуть True, если у дерева есть узлы без листов, и False, если
# их нет.
class BinaryTree:
    def __init__(self, value):
        self.key = value
        self.left_child = None
        self.right_child = None

    def insert_left(self, value):
        if self.left_child == None:
            self.left_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.left_child = self.left_child
            self.left_child = bin_tree

    def insert_right(self, value):
        if self.right_child == None:
            self.right_child = BinaryTree(value)
        else:
            bin_tree = BinaryTree(value)
            bin_tree.right_child = self.right_child
            self.right_child = bin_tree

    def hes_left_nodes(self, node):
        if node is None:
            return False
        if node.left_child is None and node.right_child is None:
            return True
        return self.hes_left_nodes(node.left_child) or self.hes_left_nodes(node.right_child)

    def has_leaf_nodes(self):
        return self.hes_left_nodes(self)


tree = BinaryTree(1)
tree.insert_left(2)
tree.insert_right(3)
result = tree.has_leaf_nodes()
print(result)


# 2. Инвертируйте двоичное дерево с помощью обхода в глубину.
class Node:
    def __init__(self, value):
        self.key = value
        self.left = None
        self.right = None


def insert_tree(node):
    if node is None:
        return
    node.left, node.right = node.right, node.left
    insert_tree(node.left)
    insert_tree(node.right)


# прямого обход дерева
def print_tree(tree):
    if tree:
        print(tree.key, end='')
        print_tree(tree.left)
        print_tree(tree.right)


#        #вызовов в обратном обходе.
# def print_tree(tree):
#    if tree:
#        print_tree(tree.left)
#        print_tree(tree.right)
#        print(tree.key, end='')
#       #симметричный обход.
# def print_tree(tree):
#    if tree:
#        print_tree(tree.left)
#        print(tree.key, end='')
#        print_tree(tree.right)
tree = Node(1)
tree.left = Node(2)
tree.right = Node(3)
tree.left.left = Node(4)
tree.right.right = Node(5)
print("Исходное дерево:")
print_tree(tree)
insert_tree(tree)
print("\nИнвертированное дерево:")
print_tree(tree)
