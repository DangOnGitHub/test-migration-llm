import pytest
from data_structures.queues.linked_queue import LinkedQueue

def test_is_empty_on_new_queue():
    queue = LinkedQueue()
    assert queue.is_empty() == True

def test_put_and_size():
    queue = LinkedQueue()
    queue.put(10)
    assert not queue.is_empty()
    assert len(queue) == 1

    queue.put(20)
    queue.put(30)
    assert len(queue) == 3

def test_get_on_single_element_queue():
    queue = LinkedQueue()
    queue.put(10)
    assert queue.get() == 10
    assert queue.is_empty() == True

def test_get_multiple_elements():
    queue = LinkedQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)

    assert queue.get() == 10
    assert queue.get() == 20
    assert queue.get() == 30
    assert queue.is_empty() == True

def test_get_on_empty_queue():
    queue = LinkedQueue()
    with pytest.raises(IndexError):
        queue.get()

def test_iter_on_empty_queue():
    queue = LinkedQueue()
    iterator = iter(queue)
    with pytest.raises(StopIteration):
        next(iterator)

def test_str_on_empty_queue():
    queue = LinkedQueue()
    assert str(queue) == ''

def test_clear_queue():
    queue = LinkedQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    queue.clear()
    assert queue.is_empty() == True
    assert len(queue) == 0

def test_queue_maintains_order():
    queue = LinkedQueue()
    for i in range(1, 101):
        queue.put(i)

    for i in range(1, 101):
        assert queue.get() == i

    assert queue.is_empty() == True

def test_size_after_operations():
    queue = LinkedQueue()
    assert len(queue) == 0

    queue.put(10)
    assert len(queue) == 1

    queue.put(20)
    assert len(queue) == 2

    queue.get()
    assert len(queue) == 1

    queue.clear()
    assert len(queue) == 0

def test_to_string():
    queue = LinkedQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)
    assert str(queue) == '10 <- 20 <- 30'

def test_to_string_on_empty_queue():
    queue = LinkedQueue()
    assert str(queue) == ''

def test_put_none():
    with pytest.raises(TypeError):
        queue = LinkedQueue()
        queue.put(None)

def test_enqueuing_after_dequeue():
    queue = LinkedQueue()
    queue.put(10)
    queue.put(20)
    queue.put(30)

    assert queue.get() == 10
    assert queue.get() == 20

    queue.put(40)
    assert next(iter(queue)) == 30
    assert len(list(queue)) == 2