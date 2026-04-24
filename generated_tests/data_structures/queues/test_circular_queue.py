import pytest
from data_structures.queues.circular_queue import CircularQueue

def test_enQueue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    assert cq.first() == 1
    assert cq.size == cq.n

def test_deQueue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    assert cq.dequeue() == 1
    assert cq.first() == 2
    assert cq.size != cq.n

def test_is_empty():
    cq = CircularQueue(3)
    assert cq.is_empty()

    cq.enqueue(1)
    assert not cq.is_empty()

def test_is_full():
    cq = CircularQueue(2)
    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.size == cq.n

    cq.dequeue()
    assert cq.size != cq.n

def test_peek():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)

    assert cq.first() == 1
    assert cq.first() == 1  # Ensure peek doesn't remove the element

def test_delete_queue():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.array = [None] * cq.n
    cq.size = 0
    cq.front = 0
    cq.rear = 0

    with pytest.raises(Exception):
        cq.first()

def test_enQueue_on_full():
    cq = CircularQueue(2)
    cq.enqueue(1)
    cq.enqueue(2)

    with pytest.raises(Exception):
        cq.enqueue(3)

def test_deQueue_on_empty():
    cq = CircularQueue(2)
    with pytest.raises(Exception):
        cq.dequeue()

def test_peek_on_empty():
    cq = CircularQueue(2)
    with pytest.raises(Exception):
        cq.first()

def test_size():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)

    assert cq.size == 2

    cq.dequeue()
    assert cq.size == 1

def test_circular_wrap_around():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.enqueue(3)

    cq.dequeue()
    cq.enqueue(4)

    assert cq.dequeue() == 2
    assert cq.dequeue() == 3
    assert cq.dequeue() == 4
    assert cq.is_empty()

def test_enQueue_deQueue_multiple_times():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.enqueue(2)
    cq.dequeue()
    cq.enqueue(3)
    cq.enqueue(4)

    assert cq.size == cq.n
    assert cq.dequeue() == 2
    assert cq.dequeue() == 3
    assert cq.dequeue() == 4
    assert cq.is_empty()

def test_multiple_wraparounds():
    cq = CircularQueue(3)
    cq.enqueue(1)
    cq.dequeue()
    cq.enqueue(2)
    cq.dequeue()
    cq.enqueue(3)
    cq.dequeue()
    cq.enqueue(4)

    assert cq.first() == 4

def test_size_during_operations():
    cq = CircularQueue(3)
    assert cq.size == 0

    cq.enqueue(1)
    cq.enqueue(2)
    assert cq.size == 2

    cq.dequeue()
    assert cq.size == 1

    cq.enqueue(3)
    cq.enqueue(4)
    assert cq.size == 3
    cq.dequeue()
    cq.dequeue()
    assert cq.size == 1