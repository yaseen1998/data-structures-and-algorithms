from left_join import __version__
from left_join.left_join import right_join,left_join
from hashtable import HashTable
import pytest

def test_version():
    assert __version__ == '0.1.0'

def test_left(synonym,antonym):
    expected = (left_join(synonym,antonym))
    actual = [['wrath', 'anger', 'delight'], ['guid', 'usher', 'follow'], ['outift', 'grab', None], ['fond', 'enamored', 'averse'], ['diligent', 'employed', 'idle']]
    assert actual == expected

def test_right(synonym,antonym):
    expected = (right_join(synonym,antonym))
    actual =[['wrath', 'delight', 'anger'], ['guid', 'follow', 'usher'], ['fond', 'averse', 'enamored'], ['flow', 'jam', None], ['diligent', 'idle', 'employed']]
    assert actual == expected

@pytest.fixture
def synonym():
    synonym = HashTable(1024)
    synonym['fond'] = 'enamored'
    synonym['wrath'] = 'anger'
    synonym['diligent'] = 'employed'
    synonym['outift'] = 'grab'
    synonym['guid'] = 'usher'
    return synonym
@pytest.fixture
def antonym():
    antonym = HashTable(1024)
    antonym['fond'] = 'averse'
    antonym['wrath'] = 'delight'
    antonym['diligent'] = 'idle'
    antonym['flow'] = 'jam'
    antonym['guid'] = 'follow'
    return antonym