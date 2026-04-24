import pytest
from data_structures.stacks.stack import Stack, StackOverflowError, StackUnderflowError


@pytest.fixture
def stack():
    return Stack[int](10)


def test_push_and_pop(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)

    assert stack.pop() == 3
    assert stack.pop() == 2
    assert stack.pop() == 1


def test_peek(stack):
    stack.push(10)
    stack.push(20)

    assert stack.peek() == 20  # Peek should return the top element
    stack.pop()  # Remove top element
    assert stack.peek() == 10  # Peek should now return the new top element


def test_is_empty(stack):
    assert stack.is_empty()  # Stack should initially be empty
    stack.push(1)
    assert not stack.is_empty()  # After pushing, stack should not be empty
    stack.pop()
    assert stack.is_empty()  # After popping, stack should be empty again


def test_make_empty(stack):
    stack.push(1)
    stack.push(2)
    stack.push(3)
    stack.stack.clear()
    assert stack.is_empty()  # Stack should be empty after makeEmpty is called
    assert stack.size() == 0  # Size should be 0 after makeEmpty


def test_size(stack):
    assert stack.size() == 0  # Initial size should be 0
    stack.push(1)
    stack.push(2)
    assert stack.size() == 2  # Size should reflect number of elements added
    stack.pop()
    assert stack.size() == 1  # Size should decrease with elements removed


def test_pop_empty_stack_throws_exception(stack):
    with pytest.raises(StackUnderflowError):
        stack.pop()  # Popping from an empty stack should throw an exception


def test_peek_empty_stack_throws_exception(stack):
    with pytest.raises(StackUnderflowError):
        stack.peek()  # Peeking into an empty stack should throw an exception


def test_mixed_operations(stack):
    # Testing a mix of push, pop, peek, and size operations in sequence
    stack.push(5)
    stack.push(10)
    stack.push(15)

    assert stack.size() == 3  # Size should reflect number of elements
    assert stack.peek() == 15  # Peek should show last element added

    stack.pop()  # Remove top element
    assert stack.peek() == 10  # New top should be 10
    assert stack.size() == 2  # Size should reflect removal

    stack.push(20)  # Add a new element
    assert stack.peek() == 20  # Top should be the last added element


def test_multiple_make_empty_calls(stack):
    # Ensures calling makeEmpty multiple times does not throw errors or misbehave
    stack.push(1)
    stack.push(2)
    stack.stack.clear()
    assert stack.is_empty()

    stack.stack.clear()
    assert stack.is_empty()
    assert stack.size() == 0