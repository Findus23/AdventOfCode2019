from day6 import parse_input, reverse_graph, count_all_orbits, get_indirect_orbits

example_input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""


def test_parse_input():
    correct = {
        'COM': {'B'}, 'B': {'C', 'G'}, 'C': {'D'}, 'D': {'I', 'E'}, 'E': {'F', 'J'}, 'G': {'H'}, 'J': {'K'}, 'K': {'L'}
    }

    assert parse_input(example_input) == correct


def test_reverse_graph():
    input = {"A": {"B"}, "B": {"C"}, "C": {"D", "E"}}
    output = {'B': 'A', 'C': 'B', 'D': 'C', 'E': 'C'}
    assert reverse_graph(input) == output


def test_get_indirect_orbits():
    input = {'B': 'A', 'C': 'B', 'D': 'C', 'E': 'C'}
    assert list(get_indirect_orbits(input, "B")) == ["A"]
    assert list(get_indirect_orbits(input, "E")) == ["C", "B", "A"]


def test_count_all_orbits():
    input = {'B': 'A', 'C': 'B', 'D': 'C', 'E': 'C'}
    assert count_all_orbits(input) == 9


def test_complete():
    child_graph = parse_input(example_input)
    parent_graph = reverse_graph(child_graph)
    correct = {
        'B': 'COM', 'C': 'B', 'G': 'B', 'D': 'C', 'E': 'D', 'I': 'D', 'J': 'E', 'F': 'E', 'H': 'G', 'K': 'J', 'L': 'K'
    }
    assert parent_graph == correct

    assert list(get_indirect_orbits(parent_graph, "D")) == ['C', 'B', 'COM']
    assert list(get_indirect_orbits(parent_graph, "L")) == ['K', 'J', 'E', 'D', 'C', 'B', "COM"]
    assert list(get_indirect_orbits(parent_graph, "COM")) == []

    assert count_all_orbits(parent_graph) == 42
