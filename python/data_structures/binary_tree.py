class Node:
    def __init__(self, value, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


class BinaryTree:
    """
    Put docstring here
    """

    def __init__(self):
        self.root = None

    def pre_order(self):

        def walk(node):
            if not node:
                return []
            return [node.value] + walk(node.left) + walk(node.right)

        return walk(self.root)

    def in_order(self):

        def walk(node):
            if not node:
                return []
            return walk(node.left) + [node.value] + walk(node.right)

        return walk(self.root)

    def post_order(self):

        def walk(node):
            if not node:
                return []
            return walk(node.left) + walk(node.right) + [node.value]

        return walk(self.root)

    def contains(self, value):

        def search(node, value):
            if node is None or node.value == value:
                return node is not None
            if value < node.value:
                return search(node.left, value)
            else:
                return search(node.right, value)

        return search(self.root, value)

class BinarySearchTree(BinaryTree):
    def add(self, value):
        def insert(node, value):
            if value < node.value:
                if node.left:
                    insert(node.left, value)
                else:
                    node.left = Node(value)
            elif value > node.value:
                if node.right:
                    insert(node.right, value)
                else:
                    node.right = Node(value)

        if self.root:
            insert(self.root, value)
        else:
            self.root = Node(value)

    def contains(self, value):

        def search(node, value):
            if node is None or node.value == value:
                return node is not None
            if value < node.value:
                return search(node.left,  value)
            else:
                return search(node.right, value)

        return search(self.root, value)
