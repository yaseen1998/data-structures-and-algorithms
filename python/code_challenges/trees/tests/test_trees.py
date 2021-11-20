from trees import __version__
from trees.trees import BinaryTree,BST,Node
import pytest
def test_version():
    assert __version__ == '0.1.0'

def test_preorder(data):
    expected =data.print_tree('preorder')
    actual = '1-2-4-5-3-6-7-8-'
    assert expected==actual

def test_inorder(data):
    expected =data.print_tree('inorder')
    actual = '4-2-5-1-6-3-7-8-'
    assert expected==actual

def test_postorder(data):
    expected =data.print_tree('postorder')
    actual = '4-5-2-6-8-7-3-1-'
    assert expected==actual

def test_empty():
    tree = BinaryTree()
    expected =tree.print_tree('empty')
    actual = 'its empty or this traversal_type is not support'
    assert expected==actual

def test_one():
    trees = BinaryTree(1)
    expected =trees.print_tree('preorder')
    actual = '1-'
    assert expected==actual

def test_binary_search(binary):
    expected = binary.print_BST()
    actual = '1-4-8-10-5-6-20-30-'
    assert expected==actual

def test_binary_contains(binary):
    expected = binary.contains(11)
    actual = False
    assert expected==actual

def test_binary_contains2(binary):
    expected = binary.contains(20)
    actual = True
    assert expected==actual


@pytest.fixture
def data():
    tree = BinaryTree(1)
    tree.root.left=Node(2)
    tree.root.right = Node(3)
    tree.root.left.left =Node(4)
    tree.root.left.right =Node(5)
    tree.root.right.left =Node(6)
    tree.root.right.right =Node(7)
    tree.root.right.right.right =Node(8)
    return tree
@pytest.fixture
def binary():
    root = BST(10)
    list1 = [20,4,30,1,8,5,6]
    for i in list1:
        (root.add(i))
    return root

