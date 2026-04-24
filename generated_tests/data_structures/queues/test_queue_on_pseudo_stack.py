import pytest
from data_structures.queues.queue_on_pseudo_stack import Queue

@pytest.fixture
def queue():
    return Queue()

def test_queue_insertion(queue):
    queue.put(1)
    queue.put(2)
    queue.put(3)
    
    assert queue.size() == 3
    assert queue.front() == 1

def test_queue_removal(queue):
    queue.put(1)
    queue.put(2)
    queue.put(3)

    assert queue.get() == 1
    assert queue.front() == 2

    assert queue.get() == 2
    assert queue.front() == 3

    assert queue.get() == 3
    with pytest.raises(IndexError):
        queue.get()

def test_peek_front(queue):
    queue.put(1)
    queue.put(2)

    assert queue.front() == 1
    assert queue.size() == 2

def test_size(queue):
    assert queue.size() == 0
    queue.put(1)
    assert queue.size() == 1
    queue.put(2)
    assert queue.size() == 2
    queue.put(3)
    assert queue.size() == 3
    queue.get()
    assert queue.size() == 2

def test_str_representation(queue):
    assert str(queue) == "<>"
    queue.put(1)
    queue.put(2)
    assert str(queue) == "<1, 2>"
    queue.get()
    assert str(queue) == "<2>"

def test_queue_state_consistency():
    queue = Queue()
    queue.put(10)
    queue.put(20)

    first_removed = queue.get()
    queue.put(30)
    queue.put(40)

    second_removed = queue.get()
    queue.put(50)

    assert first_removed == 10
    assert second_removed == 20
    assert queue.front() == 30

def test_circular_behaviour():
    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    
    queue.get()
    queue.get()
    queue.get()
    
    queue.put(4)
    queue.put(5)
    queue.put(6)

    assert queue.front() == 4

def test_single_element_operations():
    queue = Queue()
    queue.put(42)

    assert queue.front() == 42
    assert queue.get() == 42
    assert queue.size() == 0

def test_mixed_insert_remove_operations():
    queue = Queue()
    queue.put(1)
    queue.put(2)

    assert queue.get() == 1
    queue.put(3)
    queue.put(4)

    assert queue.get() == 2
    assert queue.get() == 3

    queue.put(5)
    queue.put(6)

    assert queue.front() == 4

def test_queue_wraparound():
    queue = Queue()
    queue.put(1)
    queue.put(2)
    queue.put(3)
    
    queue.get()
    queue.put(4)
    
    assert str(queue) == "<2, 3, 4>"
    
    queue.get()
    queue.put(5)
    
    assert queue.front() == 3

def test_queue_after_multiple_cycles():
    queue = Queue()
    for _ in range(3):
        for i in range(1, 4):
            queue.put(i)
        
        for _ in range(3):
            queue.get()

        assert queue.size() == 0