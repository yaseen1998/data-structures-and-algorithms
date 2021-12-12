from hastable.hashtabl import Hashtable
import pytest



def test_add(hashtable):
    hashtable.add('yaseen', 23)
    expected = 23
    actual = hashtable.get(("yaseen"))
    assert expected == actual

def test_get(hashtable):
    expected = 'how are'
    actual = hashtable.get(('YAHYA'))
    assert expected == actual

def test_get_not_exist(hashtable):
    expected = 'this element does not exist'
    actual = hashtable.get(("Ibrahim"))
    assert expected == actual

def test_group(hashtable):
    # AHMAD and HAMAD have the same hash
    expected = "[('AHMAD', 30), ('HAMAD', 55)]"
    actual = hashtable.map[hashtable.hash('AHMAD')].__str__()  # Finds where AHMAD is stored
    assert expected ==  actual

def test_retriven(hashtable):
    expected = 55
    actual = hashtable.get(("HAMAD"))
    assert expected ==  actual

def test_contain_true(hashtable):
    expected = True
    actual = hashtable.contains(("HAMAD"))
    assert expected ==  actual

def test_contain_false(hashtable):
    expected = False
    actual = hashtable.contains(("hhhhh"))
    assert expected ==  actual

@pytest.fixture
def hashtable():
    hashtable= Hashtable(1024)
    hashtable.add("AHMAD",30)
    hashtable.add("YAHYA",'how are')
    hashtable.add("HAMAD",55)
    return hashtable
