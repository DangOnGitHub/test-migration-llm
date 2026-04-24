import pytest
from data_structures.queues.queue_by_list import QueueByList


def test_add():
    queue = QueueByList[int]()
    queue.put(10)
    queue.put(20)
    assert queue.get_front() == 10  # Ensure the first added element is at the front


def test_peek():
    queue = QueueByList[int]()
    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get_front()

    queue.put(10)
    queue.put(20)

    assert queue.get_front() == 10
    queue.get()
    assert queue.get_front() == 20


def test_poll():
    queue = QueueByList[int]()
    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get()

    queue.put(10)
    queue.put(20)

    assert queue.get() == 10
    assert queue.get() == 20
    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get()


def test_is_empty():
    queue = QueueByList[int]()
    assert len(queue) == 0

    queue.put(30)
    assert len(queue) > 0
    queue.get()
    assert len(queue) == 0


def test_clear_queue_and_reuse():
    queue = QueueByList[int]()
    queue.put(5)
    queue.put(10)
    queue.get()
    queue.get()  # Remove all elements
    assert len(queue) == 0

    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get_front()

    queue.put(15)
    assert len(queue) == 1
    assert queue.get_front() == 15


def test_order_maintained():
    queue = QueueByList[str]()
    queue.put("First")
    queue.put("Second")
    queue.put("Third")

    assert queue.get() == "First"
    assert queue.get() == "Second"
    assert queue.get() == "Third"


def test_various_data_types():
    queue = QueueByList[float]()
    queue.put(1.1)
    queue.put(2.2)

    assert queue.get_front() == 1.1
    assert queue.get() == 1.1
    assert queue.get_front() == 2.2


def test_empty_poll_and_peek_behavior():
    queue = QueueByList[int]()
    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get_front()
    with pytest.raises(IndexError, match="Queue is empty"):
        queue.get()