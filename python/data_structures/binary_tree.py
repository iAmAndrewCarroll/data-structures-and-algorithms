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

    def breadth_first_traversal(self):
        if not self.root:
            return

        queue = [self.root]
        while queue:
            current = queue.pop(0)
            yield current
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)

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

    def find_maximum_value(self):
        def find_max(node):
            if node is None:
                return float('-inf')
            max_value = node.value
            left_max = find_max(node.left)
            right_max = find_max(node.right)
            if left_max > max_value:
                max_value = left_max
            if right_max > max_value:
                max_value = right_max
            return max_value

        return find_max(self.root)

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
                return search(node.left, value)
            else:
                return search(node.right, value)

        return search(self.root, value)

