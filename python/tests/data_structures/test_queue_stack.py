import pytest
from data_structures.stack import Stack
from data_structures.queue import Queue
from data_structures.invalid_operation_error import InvalidOperationError

def test_exists():
    assert Queue
    assert Stack

def test_can_enqueue_into_queue():
    queue = Queue()
    queue.enqueue(1)
    assert queue.front.value == 1

def test_can_enqueue_multiple_values_into_queue():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    assert queue.front.value == 1
    assert queue.back.value == 2

def test_can_dequeue_out_of_a_queue_the_expected_value():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    value = queue.dequeue()
    assert value == 1
    assert queue.front.value == 2

def test_can_peek_into_a_queue_seeing_the_expected_value():
    queue = Queue()
    queue.enqueue(1)
    value = queue.peek()
    assert value == 1

def test_can_successfully_empty_a_queue_after_multiple_dequeues():
    queue = Queue()
    queue.enqueue(1)
    queue.enqueue(2)
    queue.dequeue()
    queue.dequeue()
    assert queue.is_empty()

def test_can_successfully_instantiate_an_empty_queue():
    queue = Queue()
    assert queue.is_empty()

def test_calling_dequeue_or_peek_on_empty_queue_raises_exception():
    queue = Queue()
    with pytest.raises(InvalidOperationError):
        queue.dequeue()

    with pytest.raises(InvalidOperationError):
        queue.peek()
