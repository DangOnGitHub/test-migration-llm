import pytest
from data_structures.queues.circular_queue_linked_list import CircularQueueLinkedList as CircularQueue

def test_enqueue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    assert cq.first() == 1
    with pytest.raises(Exception, match="Full Queue"):
        cq.enqueue(4)

def test_dequeue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    assert cq.dequeue() == 1
    assert cq.first() == 2

def test_is_empty():
    cq = CircularQueue(3)
    assert cq.is_empty()

    cq.enqueue(1)
    assert not cq.is_empty()

def test_is_full():
    cq = CircularQueue(2)
    cq.enqueue(1)
    cq.enqueue(2)
    with pytest.raises(Exception, match="Full Queue"):
        cq.enqueue(3)

    cq.dequeue()
    assert not cq.is_empty()

def test_first():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)

    assert cq.first() == 1
    assert cq.first() == 1

def test_enqueue_on_full():
    cq = CircularQueue(2)
    cq.enqueue(1)
    cq.enqueue(2)

    with pytest.raises(Exception, match="Full Queue"):
        cq.enqueue(3)

def test_dequeue_on_empty():
    cq = CircularQueue(2)
    with pytest.raises(Exception, match="Empty Queue"):
        cq.dequeue()

def test_first_on_empty():
    cq = CircularQueue(2)
    with pytest.raises(Exception, match="Empty Queue"):
        cq.first()

def test_circular_wrap_around():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    assert cq.dequeue() == 1
    cq.enqueue(4)

    assert cq.dequeue() == 2
    assert cq.dequeue() == 3
    assert cq.dequeue() == 4
    assert cq.is_empty() == True

def test_enqueue_dequeue_multiple_times():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.dequeue()
    cq.enqueue(3)
    cq.enqueue(4)

    assert cq.dequeue() == 2
    assert cq.dequeue() == 3
    assert cq.dequeue() == 4
    assert cq.is_empty() == True

def test_multiple_wrap_around():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.dequeue()
    cq.enqueue(2)
    cq.dequeue()
    cq.enqueue(3)
    cq.dequeue()
    cq.enqueue(4)

    assert cq.first() == 4

# Since there's no direct size method in this implementation, we don't test size assertions