import pytest
from sorts.topological_sort import topological_sort

def test_success():
    edges = {
        "shirt": ["tie", "belt"],
        "tie": ["jacket"],
        "belt": ["jacket"],
        "watch": [],
        "undershorts": ["pants", "shoes"],
        "shoes": [],
        "socks": ["shoes"],
        "jacket": [],
        "pants": ["belt", "shoes"],
    }
    vertices = ["shirt", "tie", "belt", "watch", "undershorts", "shoes", "socks", "jacket", "pants"]
    expected = ["socks", "undershorts", "pants", "shoes", "watch", "shirt", "belt", "tie", "jacket"]

    def topological_wrapper(start):
        return topological_sort(start, [], [])

    with pytest.raises(Exception):
        topological_wrapper("missing node")

    visited = []
    sort = []
    for vertex in vertices:
        if vertex not in visited:
            sort = topological_sort(vertex, visited, sort)
    assert sort == expected

def test_failure():
    edges = {
        "1": ["2", "3", "8"],
        "2": ["4"],
        "3": ["5"],
        "4": ["6"],
        "5": ["4", "7", "8"],
        "6": ["2"],
        "7": [],
        "8": [],
    }
    vertices = ["1", "2", "3", "4", "5", "6", "7", "8"]

    def topological_wrapper(start):
        return topological_sort(start, [], [])

    visited = []
    sort = []
    for vertex in vertices:
        if vertex not in visited:
            with pytest.raises(RuntimeError, match=r"This graph contains a cycle. No linear ordering is possible. Back edge: 6 -> 2"):
                sort = topological_sort(vertex, visited, sort)

def test_empty_graph():
    edges.clear()
    vertices.clear()

    visited = []
    sort = []
    for vertex in vertices:
        if vertex not in visited:
            sort = topological_sort(vertex, visited, sort)
    assert sort == []

def test_single_node():
    edges.clear()
    vertices.clear()
    edges["A"] = []
    vertices.append("A")

    visited = []
    sort = []
    for vertex in vertices:
        if vertex not in visited:
            sort = topological_sort(vertex, visited, sort)
    assert sort == ["A"]