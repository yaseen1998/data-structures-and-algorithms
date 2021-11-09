from linked_list_zip import __version__
from linked_list_zip.linked_list_zip import LinkedZip


def test_version():
    assert __version__ == '0.1.0'

def test_Samesize():
    ll= LinkedZip()
    ll.Zip([1,2,3,4],[5,6,7,8])
    expected = 'head -> [1] -> [5] -> [2] -> [6] -> [3] -> [7] -> [4] -> [8] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_twoList_empty():
    ll= LinkedZip()
    ll.Zip([],[])
    expected = 'the list is empty'
    actual = ll.to_string()
    assert expected == actual

def test_first_empty():
    ll= LinkedZip()
    ll.Zip([],[1,2,3,4])
    expected = 'head -> [1] -> [2] -> [3] -> [4] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_second_empty():
    ll= LinkedZip()
    ll.Zip([1,2,3,4],[])
    expected = 'head -> [1] -> [2] -> [3] -> [4] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_second_longer():
    ll= LinkedZip()
    ll.Zip([1,2,3,4],[5,6,7,8,9])
    expected = 'head -> [1] -> [5] -> [2] -> [6] -> [3] -> [7] -> [4] -> [8] -> [9] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_first_longer():
    ll= LinkedZip()
    ll.Zip([1,2,3,4,9],[5,6,7,8])
    expected = 'head -> [1] -> [5] -> [2] -> [6] -> [3] -> [7] -> [4] -> [8] -> [9] -> x'
    actual = ll.to_string()
    assert expected == actual


