import pytest

from stack_queue_pseudo.stack import Stack

from stack_queue_pseudo.stack_queue_pseudo import Pseudo_Queue

def test_enqueu(data):
    actual = data.enqueue(4)
    expected = "[4]->[3]->[2]->[1]"
    assert actual == expected

def test_enqueu_empty():
    stack= Stack()
    data=Pseudo_Queue(stack)
    actual = data.enqueue(4)
    expected = "[4]"
    assert actual == expected

def test_dequeue(data):
    actual = data.dequeue()
    expected = 1
    assert actual == expected

@pytest.fixture
def data():
    stack= Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    pseudo_queue = Pseudo_Queue(stack)
    return pseudo_queue
