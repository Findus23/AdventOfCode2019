from typing import Iterator, Dict, Set, List


Node = str
ChildGraph = Dict[Node, Set[Node]]
ParentGraph = Dict[Node, Node]


def parse_input(input: str) -> ChildGraph:
    data: ChildGraph = {}
    for line in input.split("\n"):
        if ")" not in line:
            continue
        a, b = line.split(")")
        if a not in data:
            data[a] = set()
        data[a].add(b)
    return data


def reverse_graph(graph: ChildGraph) -> ParentGraph:
    output: ParentGraph = {}
    for parent, children in graph.items():
        for child in children:
            output[child] = parent
    return output


def get_indirect_orbits(graph: ParentGraph, node: Node) -> Iterator[Node]:
    while True:
        try:
            parent = graph[node]
        except KeyError:
            break
        yield parent
        node = parent


def count_all_orbits(graph: ParentGraph) -> int:
    orbits = 0
    for parent, child in graph.items():
        all_children = list(get_indirect_orbits(graph, parent))
        orbits += len(all_children)

    return orbits


def part1() -> int:
    with open("6/input.txt") as f:
        input = f.read()
    gr = parse_input(input)
    parent_graph = reverse_graph(gr)
    return count_all_orbits(parent_graph)


def get_common_ancestor(a: List[Node], b: List[Node]) -> Node:
    node = "none"
    i = -1
    while a[i] == b[i]:
        node = a[i]
        i -= 1
    return node


def calculate_distance_to_santa(pg: ParentGraph) -> int:
    your_parents = list(get_indirect_orbits(pg, "YOU"))
    santa_parents = list(get_indirect_orbits(pg, "SAN"))
    common_ancestor = get_common_ancestor(your_parents, santa_parents)

    up = your_parents.index(common_ancestor)
    down = santa_parents.index(common_ancestor)

    return up + down


def part2() -> int:
    with open("6/input.txt") as f:
        input = f.read()
    gr = parse_input(input)
    parent_graph = reverse_graph(gr)
    return calculate_distance_to_santa(parent_graph)


if __name__ == '__main__':
    # print(part1())
    print(part2())
