import pytest
from data_structures.binary_tree import BinarySearchTree, BinaryTree, Node

def test_exists():
    assert BinaryTree

def test_pre_order(tree):
    actual = tree.pre_order()
    expected = ["a", "b", "d", "e", "c", "f", "g"]
    assert actual == expected

def test_in_order(tree):
    actual = tree.in_order()
    expected = ["d", "b", "e", "a", "f", "c", "g"]
    assert actual == expected

def test_post_order(tree):
    actual = tree.post_order()
    expected = ["d", "e", "b", "f", "g", "c", "a"]
    assert actual == expected

def test_instantiate_empty_tree():
    tree = BinaryTree()
    assert tree.root is None

def test_instantiate_single_root_node():
    tree = BinaryTree()
    tree.root = Node("a")
    assert tree.root.value == "a"

def test_add_left_and_right_child_to_node():
    tree = BinarySearchTree()
    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    assert tree.root.value == "a"

@pytest.fixture
def tree():
    """
          a
      b      c
    d  e    f  g
    """

    tree = BinarySearchTree()

    tree.root = Node("a")
    tree.root.left = Node("b")
    tree.root.right = Node("c")
    tree.root.left.left = Node("d")
    tree.root.left.right = Node("e")
    tree.root.right.left = Node("f")
    tree.root.right.right = Node("g")

    return tree

def test_contains_existing_node(tree):
    assert tree.contains("a") is True
    assert tree.contains("b") is True
    assert tree.contains("c") is True


def test_contains_non_existing_node(tree):
    assert tree.contains("z") is False
    assert tree.contains("x") is False
    assert tree.contains("y") is False
    assert tree.contains("w") is False

