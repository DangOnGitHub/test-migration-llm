import pytest
from data_structures.queues.queue_by_two_stacks import QueueByTwoStacks


@pytest.fixture
def queue():
    return QueueByTwoStacks[int]()


def test_empty_queue(queue):
    assert len(queue) == 0


def test_enqueue(queue):
    queue.put(10)
    queue.put(20)
    assert len(queue) == 2


def test_dequeue(queue):
    queue.put(10)
    queue.put(20)
    queue.put(30)
    assert queue.get() == 10
    assert queue.get() == 20
    assert queue.get() == 30


def test_interleaved_operations(queue):
    queue.put(10)
    queue.put(20)
    assert queue.get() == 10
    queue.put(30)
    assert queue.get() == 20
    assert queue.get() == 30


def test_queue_size(queue):
    assert len(queue) == 0
    queue.put(1)
    assert len(queue) == 1
    queue.put(2)
    queue.put(3)
    assert len(queue) == 3
    queue.get()
    assert len(queue) == 2


def test_empty_queue_exception(queue):
    with pytest.raises(IndexError):
        queue.get()


def test_dequeue_all_elements(queue):
    for i in range(1, 6):
        queue.put(i)
    for i in range(1, 6):
        assert queue.get() == i
    assert len(queue) == 0


def test_large_number_of_operations(queue):
    n = 1000
    for i in range(n):
        queue.put(i)
    for i in range(n):
        assert queue.get() == i
    assert len(queue) == 0


def test_refill_during_dequeue(queue):
    queue.put(1)
    queue.put(2)
    assert queue.get() == 1
    queue.put(3)
    queue.put(4)
    assert queue.get() == 2
    assert queue.get() == 3
    assert queue.get() == 4


def test_alternating_put_and_get(queue):
    queue.put(1)
    assert queue.get() == 1
    queue.put(2)
    queue.put(3)
    assert queue.get() == 2
    queue.put(4)
    assert queue.get() == 3
    assert queue.get() == 4


def test_size_stability(queue):
    queue.put(100)
    size1 = len(queue)
    size2 = len(queue)
    assert size1 == size2


def test_multiple_empty_dequeues(queue):
    with pytest.raises(IndexError):
        queue.get()
    with pytest.raises(IndexError):
        queue.get()


def test_queue_with_strings():
    queue = QueueByTwoStacks[str]()
    queue.put("a")
    queue.put("b")
    assert queue.get() == "a"
    assert queue.get() == "b"