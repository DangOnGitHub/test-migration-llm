import pytest
from data_structures.queues.priority_queue_using_list import ElementPriorityQueue, UnderFlowError, OverFlowError

def test_pq_insertion():
    epq = ElementPriorityQueue()
    epq.enqueue(2)
    assert epq.queue == [2]

    epq.enqueue(5)
    epq.enqueue(3)
    assert epq.queue == [2, 5, 3]

    epq.enqueue(10)
    assert epq.queue == [2, 5, 3, 10]

def test_pq_deletion():
    epq = ElementPriorityQueue()
    epq.enqueue(2)
    epq.enqueue(5)
    epq.enqueue(3)
    epq.enqueue(10)

    assert epq.dequeue() == 2
    assert epq.dequeue() == 3
    assert epq.dequeue() == 5
    assert epq.queue == [10]

def test_pq_extra():
    epq = ElementPriorityQueue()
    assert len(epq.queue) == 0
    epq.enqueue(2)
    epq.enqueue(5)
    epq.enqueue(3)
    epq.enqueue(10)
    assert len(epq.queue) == 4

    assert epq.dequeue() == 2
    assert len(epq.queue) == 3
    assert epq.dequeue() == 3
    assert epq.dequeue() == 5
    assert len(epq.queue) == 1

def test_insert_until_full():
    epq = ElementPriorityQueue()
    for _ in range(100):
        epq.enqueue(1)
    with pytest.raises(OverFlowError):
        epq.enqueue(1)

def test_remove_from_empty():
    epq = ElementPriorityQueue()
    with pytest.raises(UnderFlowError):
        epq.dequeue()

def test_insert_duplicate_values():
    epq = ElementPriorityQueue()
    epq.enqueue(5)
    epq.enqueue(5)
    epq.enqueue(3)
    assert epq.queue == [5, 5, 3]

    assert epq.dequeue() == 3
    assert epq.dequeue() == 5
    assert epq.queue == [5]

def test_size_after_insert_and_remove():
    epq = ElementPriorityQueue()
    assert len(epq.queue) == 0
    epq.enqueue(2)
    assert len(epq.queue) == 1
    epq.enqueue(10)
    assert len(epq.queue) == 2
    epq.dequeue()
    assert len(epq.queue) == 1
    epq.dequeue()
    assert len(epq.queue) == 0

def test_insert_and_remove_all():
    epq = ElementPriorityQueue()
    epq.enqueue(8)
    epq.enqueue(1)
    epq.enqueue(6)
    assert len(epq.queue) == 3
    epq.dequeue()
    epq.dequeue()
    epq.dequeue()
    assert len(epq.queue) == 0