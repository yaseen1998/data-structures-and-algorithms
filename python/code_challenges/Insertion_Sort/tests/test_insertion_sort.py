from insertion_sort import __version__
from insertion_sort.insertion_sort import InsertionSort



def test_insertion():
    expect = InsertionSort([8,4,23,42,16,15])
    actual = [4, 8, 15, 16, 23, 42]
    assert expect == actual
def test_Reverse_sorted():
    expect = InsertionSort([20,18,12,8,5,-2])
    actual = [-2, 5, 8, 12, 18, 20]
    assert expect == actual
def test_Few_uniques():
    expect = InsertionSort([5,12,7,5,5,7])
    actual = [5, 5, 5, 7, 7, 12]
    assert expect == actual
def test_Nearly_sorted():
    expect = InsertionSort([2,3,5,7,13,11])
    actual = [2, 3, 5, 7, 11, 13]
    assert expect == actual
