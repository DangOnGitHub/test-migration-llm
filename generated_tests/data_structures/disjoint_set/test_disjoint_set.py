import pytest
from data_structures.disjoint_set.disjoint_set import Node, make_set, union_set, find_set

def test_make_set():
    node = Node(1)
    make_set(node)
    assert node.parent == node

def test_union_find_set():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    make_set(node1)
    make_set(node2)
    make_set(node3)
    make_set(node4)

    union_set(node1, node2)
    union_set(node3, node2)
    union_set(node3, node4)
    union_set(node1, node3)

    root1 = find_set(node1)
    root2 = find_set(node2)
    root3 = find_set(node3)
    root4 = find_set(node4)

    assert node1.parent == node1
    assert node2.parent == node1
    assert node3.parent == node1
    assert node4.parent == node1

    assert root1 == node1
    assert root2 == node1
    assert root3 == node1
    assert root4 == node1

    assert node1.rank == 1
    assert node2.rank == 0
    assert node3.rank == 0
    assert node4.rank == 0

def test_find_set_on_single_node():
    node = Node("A")
    make_set(node)
    assert find_set(node) == node

def test_union_already_connected_nodes():
    node1, node2, node3 = Node(1), Node(2), Node(3)
    make_set(node1)
    make_set(node2)
    make_set(node3)

    union_set(node1, node2)
    union_set(node2, node3)

    union_set(node1, node3)

    root = find_set(node1)
    assert find_set(node2) == root
    assert find_set(node3) == root

def test_rank_increase():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    make_set(node1)
    make_set(node2)
    make_set(node3)
    make_set(node4)

    union_set(node1, node2)
    union_set(node3, node4)
    union_set(node1, node3)

    assert find_set(node1).rank == 2

def test_multiple_make_sets():
    node1, node2, node3 = Node(1), Node(2), Node(3)
    make_set(node1)
    make_set(node2)
    make_set(node3)

    assert node1 != node2
    assert node2 != node3
    assert node1 != node3

    assert node1.parent == node1
    assert node2.parent == node2
    assert node3.parent == node3

def test_path_compression():
    node1, node2, node3 = Node(1), Node(2), Node(3)
    make_set(node1)
    make_set(node2)
    make_set(node3)

    union_set(node1, node2)
    union_set(node2, node3)

    root = find_set(node3)
    assert root == node1
    assert node3.parent == node1

def test_union_by_rank_smaller_to_larger():
    node1, node2, node3 = Node(1), Node(2), Node(3)
    make_set(node1)
    make_set(node2)
    make_set(node3)

    union_set(node1, node2)
    assert node1.rank == 1
    assert node2.rank == 0

    union_set(node3, node1)
    assert find_set(node3) == node1
    assert node1.rank == 1

def test_union_by_rank_equal_ranks():
    node1, node2, node3, node4 = Node(1), Node(2), Node(3), Node(4)
    make_set(node1)
    make_set(node2)
    make_set(node3)
    make_set(node4)

    union_set(node1, node2)
    union_set(node3, node4)
    assert node1.rank == 1
    assert node3.rank == 1

    union_set(node1, node3)
    root = find_set(node1)
    assert root.rank == 2

def test_large_chain_path_compression():
    node1, node2, node3, node4, node5 = Node(1), Node(2), Node(3), Node(4), Node(5)
    make_set(node1)
    make_set(node2)
    make_set(node3)
    make_set(node4)
    make_set(node5)

    union_set(node1, node2)
    union_set(node2, node3)
    union_set(node3, node4)
    union_set(node4, node5)

    root = find_set(node5)

    assert node5.parent == root
    assert node4.parent == root
    assert node3.parent == root
    assert node2.parent == root
    assert node1.parent == root

def test_multiple_disjoint_sets():
    node1, node2, node3, node4, node5, node6 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6)
    make_set(node1)
    make_set(node2)
    make_set(node3)
    make_set(node4)
    make_set(node5)
    make_set(node6)

    union_set(node1, node2)
    union_set(node2, node3)

    union_set(node4, node5)
    union_set(node5, node6)

    assert find_set(node1) == find_set(node2)
    assert find_set(node2) == find_set(node3)
    assert find_set(node4) == find_set(node5)
    assert find_set(node5) == find_set(node6)

    assert find_set(node1) != find_set(node4)
    assert find_set(node3) != find_set(node6)

def test_empty_values():
    empty_node = Node("")
    null_node = Node(None)
    make_set(empty_node)
    make_set(null_node)

    assert find_set(empty_node) == empty_node
    assert find_set(null_node) == null_node

    union_set(empty_node, null_node)
    assert find_set(empty_node) == find_set(null_node)