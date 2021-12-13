from tree_intersection.binary_tree import Binary_tree
from tree_intersection.tree_intersection import Intersection


def test_false():
    tree1 = Binary_tree(20)
    tree1.add(40)
    tree1.add(10)
    tree1.add(15)
    tree1.add(30)
    result1 = tree1.print_BST()

    tree2 = Binary_tree(21)
    tree2.add(4)
    tree2.add(19)
    tree2.add(45)
    tree2.add(31)
    result2 = tree2.print_BST()

    hash = Intersection()
    hash.add(result1)
    excpect = (hash.contains(result2))
    actual = 'no inersection'
    assert actual == excpect

def test_true():
    tree1 = Binary_tree(20)
    tree1.add(40)
    tree1.add(10)
    tree1.add(15)
    tree1.add(30)
    result1 = tree1.print_BST()

    tree2 = Binary_tree(20)
    tree2.add(4)
    tree2.add(19)
    tree2.add(45)
    tree2.add(30)
    result2 = tree2.print_BST()

    hash = Intersection()
    hash.add(result1)
    excpect = (hash.contains(result2))
    actual = [20,30]
    assert actual == excpect

