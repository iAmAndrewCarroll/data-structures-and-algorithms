from data_structures.binary_tree import BinaryTree
from collections import deque


def breadth_first(tree):
    if not tree.root:
        return[]

    result = []
    queue = deque()
    queue.append(tree.root)

    while queue:
        node = queue.popleft()
        result.append(node.value)

        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

    return result
