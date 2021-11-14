from stack_and_queue.stack import Stack

from stack_and_queue.queue import Queue

from stack_and_queue.pseudo_queue import Pseudo_Queue

import pytest
def test_push_one_element():
    stack = Stack()
    stack.push(100)
    excepted =100
    actual = stack.peek()
    assert excepted == actual


def test_push_multi_element():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    excepted =3
    actual = stack.peek()
    assert actual == excepted

def test_pop():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.pop()
    excepted =2
    actual = stack.peek()
    assert actual == excepted

def test_pop_empty():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    stack.pop()
    stack.pop()
    excepted ='Stack is Empty'
    actual = stack.peek()
    assert actual == excepted


def test_peek():
    stack = Stack()
    stack.push(1)
    stack.push(2)
    expected = 2
    actual = stack.peek()
    assert actual == expected


def test_init_empty():
    stack = Stack()
    expected = None
    actual = stack.topval
    assert expected == actual


def test_empty_stack():
    stack = Stack()
    expected = "Stack is Empty"
    assert expected == stack.peek()




def test_EnQueue_one_element():
    queue = Queue()
    queue.EnQueue(100)
    excepted =100
    actual = queue.peek()
    assert excepted == actual


def test_queue_multi_element():
    queue = Queue()
    queue.EnQueue(1)
    queue.EnQueue(2)
    queue.EnQueue(3)
    excepted =1
    actual = queue.peek()
    assert actual == excepted

def test_DeQueue():
    queue = Queue()
    queue.EnQueue(1)
    queue.EnQueue(2)
    queue.EnQueue(3)
    queue.DeQueue()
    excepted =2
    actual = queue.peek()
    assert actual == excepted

def test_DeQueue():
    queue = Queue()
    queue.EnQueue(1)
    queue.EnQueue(2)
    queue.DeQueue()
    queue.DeQueue()
    excepted ="queue is Empty"
    actual = queue.peek()
    assert actual == excepted


def test_queue_peek():
    queue = Queue()
    queue.EnQueue(1)
    queue.EnQueue(2)
    excepted =1
    actual = queue.peek()
    assert actual == excepted

def test_init_queue():
    queue = Queue()
    expected = None
    actual = queue.front
    assert expected == actual


def test_empty_queue():
    queue = Queue()
    expected = "queue is Empty"
    assert expected == queue.peek()

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
