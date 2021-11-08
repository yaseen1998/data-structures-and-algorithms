import pytest
from linked_list_insertions import __version__
from linked_list_insertions.linked_list_insertions import LinkedList

def test_version():
    assert __version__ == '0.1.0'

def test_append_node():
    ll= LinkedList()
    ll.append(1)
    print(ll.to_string())
    expected = 'head -> [1] -> x'
    actual = ll.to_string()
    assert expected == actual


def test_append_multiplenode():
    ll= LinkedList()
    ll.append(1)
    ll.append('hi')
    ll.append(2)
    print(ll.to_string())
    expected = 'head -> [1] -> [hi] -> [2] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_inserbefore():
    ll= LinkedList()
    ll.append(1)
    ll.append('hi')
    ll.append(2)
    ll.append(3)
    ll.insertbefore(2,'hello')
    print(ll.to_string())
    expected = 'head -> [1] -> [hi] -> [hello] -> [2] -> [3] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_inserbefore_firstnode():
    ll= LinkedList()
    ll.append(1)
    ll.append('hi')
    ll.append(2)
    ll.append(3)
    ll.insertbefore(1,'hello')
    print(ll.to_string())
    expected = 'head -> [hello] -> [1] -> [hi] -> [2] -> [3] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_inserafter():
    ll= LinkedList()
    ll.append(1)
    ll.append('hi')
    ll.append(2)
    ll.append(3)
    ll.insertafter(2,'hello')
    print(ll.to_string())
    expected = 'head -> [1] -> [hi] -> [2] -> [hello] -> [3] -> x'
    actual = ll.to_string()
    assert expected == actual

def test_inserafter_lastnode():
    ll= LinkedList()
    ll.append(1)
    ll.append('hi')
    ll.append(2)
    ll.append(3)
    ll.insertafter(3,'hello')
    print(ll.to_string())
    expected = 'head -> [1] -> [hi] -> [2] -> [3] -> [hello] -> x'
    actual = ll.to_string()
    assert expected == actual
