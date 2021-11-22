from tree_breadth_first import __version__
from tree_breadth_first.tree_breadth_first import Node,printLevelOrder

def test_version():
    assert __version__ == '0.1.0'

def test_bredthe1():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(7)
    root.left.right = Node(5)
    expected = printLevelOrder(root)
    actual ='1-2-3-4-5-6-7-'
    assert actual == expected

def test_bredthe2():
    root = Node(1)
    expected = printLevelOrder(root)
    actual ='1-'
    assert actual == expected

def test_bredthe3():
    root = Node()
    expected = printLevelOrder(root)
    actual ='empty'
    assert actual == expected
