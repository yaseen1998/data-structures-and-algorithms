from tree_max import __version__
from tree_max.tree_max import Node,max
import pytest

def test_version():
    assert __version__ == '0.1.0'


def test_max(data):
    expected =max(data)
    actual = 8
    assert expected==actual

def test_empty():
    tree = Node()
    expected =max(tree)
    actual = 'the tree is empty'
    assert expected==actual

def test_one():
    tree = Node(1)
    expected =max(tree)
    actual = 1
    assert expected==actual

@pytest.fixture
def data():
    tree = Node(1)
    tree.left=Node(2)
    tree.right = Node(3)
    tree.left.left =Node(4)
    tree.left.right =Node(5)
    tree.right.left =Node(6)
    tree.right.right =Node(7)
    tree.right.right.right =Node(8)
    return tree
