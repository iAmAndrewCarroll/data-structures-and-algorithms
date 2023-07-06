# import sys
# sys.path.append('/Users/andrewcarroll/Code-Fellows/projects/data-structures-and-algorithms/python')
# sys.path.append('/Users/andrewcarroll/Code-Fellows/projects/data-structures-and-algorithms/python/tests/code_challenges/test_tree_fizz_buzz.py')
# # from code_challenges.data_structures.binary_tree import BinaryTree
# from data_structures.kary_tree import KaryTree, Node
# from data_structures.binary_tree import BinaryTree
# import copy

# def fizz_buzz_tree(kary_tree):
#     # create a copy of the tree using the same structure by implementing a copy method
#     if kary_tree is None:
#         return None
#     kary_tree_copy = copy.deepcopy(kary_tree)

#     def fizz_buzz(root):
#         print("this is the value: ", root.value)
#         if root.value % 3 == 0 and root.value % 5 == 0:
#             root.value = "FizzBuzz"
#         elif root.value % 3 == 0:
#             root.value = "Fizz"
#         elif root.value % 5 == 0:
#             root.value = "Buzz"
#         elif root.value % 3 != 0 and root.value % 5 != 0:
#             root.value = str(root.value)
#         # print("this is the value: ", root.value)
#         for k_child in root.children:
#             fizz_buzz(k_child)

#     fizz_buzz(kary_tree_copy.root)
#     return kary_tree_copy

from data_structures.binary_tree import BinaryTree
from data_structures.kary_tree import KaryTree, Node


# class TreeNode:
#     def __init__(self, value=None):
#         self.value = value
#         self.children = []

def fizz_buzz_tree(tree):
    if not tree.root:
        return None

    new_tree = KaryTree(Node(None))  # Create a new KaryTree with the modified TreeNode
    process_node(tree.root, new_tree.root)  # Pass the root nodes to process

    return new_tree

def process_node(current_node, new_node):
    # print("current_node.value: ", current_node.value)
    if current_node.value % 3 == 0 and current_node.value % 5 == 0:
        new_node.value = "FizzBuzz"
    elif current_node.value % 3 == 0:
        new_node.value = "Fizz"
    elif current_node.value % 5 == 0:
        new_node.value = "Buzz"
    else:
        new_node.value = str(current_node.value)
    # print("new_node.value: ", new_node.value)
    for child_node in current_node.children:
        # print("child_node.value: ", child_node.value)
        new_child_node = Node(None)
        # print("new_child_node.value: ", new_child_node.value)
        new_node.children.append(new_child_node)
        process_node(child_node, new_child_node)

if __name__ == "__main__":
    tree = KaryTree()
    one = Node(1)
    two = Node(2)
    three = Node(3)
    four = Node(4)
    five = Node(5)
    six = Node(6)
    seven = Node(7)
    eight = Node(8)
    nine = Node(9)
    ten = Node(10)
    eleven = Node(11)
    twelve = Node(12)
    thirteen = Node(13)
    fourteen = Node(14)
    fifteen = Node(15)

    """
                            1
                2                       3
            4  5  6               7     8          9
        10  11 12              13            14   15
    """

    one.children = [two, three]
    two.children = [four, five, six]
    three.children = [seven, eight, nine]
    four.children = [ten]
    five.children = [eleven]
    six.children = [twelve]
    seven.children = [thirteen]
    nine.children = [fourteen, fifteen]

    fizzy_tree = KaryTree(one)
    print("fizzy one: ", fizz_buzz_tree(fizzy_tree))
    print("fizzy two: ", fizzy_tree.breadth_first())

    # return new_node


    # def traverse(node):
    #     if isinstance(node, BinaryTree):
    #         new_node = Node(fizz_buzz(node.value))
    #         new_node.left = traverse(node.left)
    #         new_node.right = traverse(node.right)
    #     elif isinstance(node, KaryTree):
    #         new_node = KaryTree(Node(fizz_buzz(node.root.value)))
    #         new_node.root.children = [traverse(child) for child in node.root.children]
    #     else:
    #         new_node = Node(fizz_buzz(node.value))
    #         new_node.children = [traverse(child) for child in node.children]
    #     return new_node

    # if not tree.root:
    #     return KaryTree()

    # new_tree = KaryTree(traverse(tree.root))
    # return new_tree

# result_tree = fizz_buzz_tree(tree)
# print(result_tree)
