from typing import Tuple, List


def parse_path(path: str):
    commands = path.split(",")

    return [(c[0], int(c[1:])) for c in commands]


def record_path(path) -> List[Tuple[int, int]]:
    pos = [0, 0]
    poslist = []
    for direction, length in path:
        while length > 0:
            if direction == "U":
                pos[1] += 1
            elif direction == "D":
                pos[1] -= 1
            elif direction == "R":
                pos[0] += 1
            elif direction == "L":
                pos[0] -= 1
            else:
                raise ValueError(f"invalid direction: {direction}")
            poslist.append((pos[0], pos[1]))
            length -= 1
    return poslist


def manhatten_distance(point: Tuple[int, int]) -> int:
    return abs(point[0]) + abs(point[1])


def closest_crossing(first_path, second_path) -> int:
    p1 = record_path(first_path)
    p2 = record_path(second_path)
    commons = set(p1).intersection(set(p2))
    min_dist = 100000
    for crossing in commons:
        dist = manhatten_distance(crossing)
        if dist < min_dist:
            min_dist = dist
    return min_dist


def shortest_signal(first_path, second_path) -> int:
    p1 = record_path(first_path)
    p2 = record_path(second_path)
    commons = set(p1).intersection(set(p2))
    shortest = 10000000
    for crossing in commons:
        total = 0
        for path in [p1, p2]:
            i = 0
            for segment in path:
                i += 1
                if segment == crossing:
                    total += i
                    break
        if total < shortest:
            shortest = total

    return shortest


def part1() -> int:
    with open("3/input.txt") as f:
        w1, w2 = f.readlines()
    return closest_crossing(parse_path(w1), parse_path(w2))


def part2() -> int:
    with open("3/input.txt") as f:
        w1, w2 = f.readlines()
    return shortest_signal(parse_path(w1), parse_path(w2))


if __name__ == '__main__':
    print(part1())
    print(part2())
