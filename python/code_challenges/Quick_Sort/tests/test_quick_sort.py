from quick_sort import __version__
from quick_sort.quick_sort import QuicSort


def test_version():
    assert __version__ == '0.1.0'

def test_default():
    expected= QuicSort([8,4,23,42,16,15])
    actual = [4, 8, 15, 16, 23, 42]
    assert expected == actual

def test_reverse():
    expected= QuicSort([20,18,12,8,5,-2])
    actual = [-2, 5, 8, 12, 18, 20]
    assert expected == actual

def test_Few_uniques():
    expected= QuicSort([5,12,7,5,5,7])
    actual = [5, 5, 5, 7, 7, 12]
    assert expected == actual

def test_Nearly_sorted():
    expected= QuicSort([2,3,5,7,13,11])
    actual = [2, 3, 5, 7, 11, 13]
    assert expected == actual
