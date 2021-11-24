from tree_fizz_buzz import __version__
from tree_fizz_buzz.tree_fizz_buzz import Node,fizz_buzz


def test_version():
    assert __version__ == '0.1.0'

def test_fizz():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(6)
    root.right.right = Node(8)
    root.left.right = Node(9)
    expected = fizz_buzz(root)
    actual = '1-2-Fizz-4-Fizz-Fizz-8-'
    assert actual == expected

def test_buzz():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(5)
    root.left.left = Node(4)
    root.right.left = Node(10)
    root.right.right = Node(8)
    root.left.right = Node(20)
    expected = fizz_buzz(root)
    actual = '1-2-Buzz-4-Buzz-Buzz-8-'
    assert actual == expected

def test_multi():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.right.left = Node(10)
    root.right.right = Node(8)
    root.left.right = Node(15)
    expected = fizz_buzz(root)
    actual = '1-2-Fizz-4-FizzBuzz-Buzz-8-'
    assert actual == expected

def test_fizz_buzz():
    root = Node(1)
    root.left = Node(2)
    root.right = Node(15)
    expected = fizz_buzz(root)
    actual = '1-2-FizzBuzz-'
    assert actual == expected
