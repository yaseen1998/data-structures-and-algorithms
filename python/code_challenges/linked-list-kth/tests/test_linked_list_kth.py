from linked_list_kth import __version__
from linked_list_kth.linked_list_kth import LinkeKth

def test_version():
    assert __version__ == '0.1.0'

def test_greater():
    ll= LinkeKth()
    ll.array([1,3,8,2])
    ll.Kthindex(6)
    expected = 'the value is longer then array  '
    actual = 'the value is longer then array  '
    assert expected == actual

def test_same():
    ll= LinkeKth()
    ll.array([1,3,8,2])
    ll.Kthindex(3)
    expected = 1
    actual = 1
    assert expected == actual

def test_first():
    ll= LinkeKth()
    ll.array([1,3,8,2])
    ll.Kthindex(0)
    expected = 2
    actual = 2
    assert expected == actual

def test_middle():
    ll= LinkeKth()
    ll.array([1,3,8,2])
    ll.Kthindex(2)
    expected = 2
    actual = 2
    assert expected == actual

def test_size():
    ll= LinkeKth()
    ll.array([1])
    ll.Kthindex(0)
    expected = 1
    actual = 1
    assert expected == actual

def test_negative():
    ll= LinkeKth()
    ll.array([1,3,8,2])
    ll.Kthindex(-3)
    expected = 'the value is not exist'
    actual = 'the value is not exist'
    assert expected == actual


