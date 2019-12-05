from day3 import parse_path, manhatten_distance, closest_crossing, part1, shortest_signal, part2


def test_parse_path():
    assert parse_path("R8,U5,L5,D3") == [('R', 8), ('U', 5), ('L', 5), ('D', 3)]


def test_manhatten_distance():
    assert manhatten_distance((1, 4)) == 5


def test_closest_crossing():
    assert closest_crossing(parse_path("R8,U5,L5,D3"), parse_path("U7,R6,D4,L4")) == 6
    assert closest_crossing(parse_path("R75,D30,R83,U83,L12,D49,R71,U7,L72"),
                            parse_path("U62,R66,U55,R34,D71,R55,D58,R83")) == 159
    assert closest_crossing(parse_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"),
                            parse_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 135


def test_shortest_signal():
    assert shortest_signal(parse_path("R8,U5,L5,D3"), parse_path("U7,R6,D4,L4")) == 30
    assert shortest_signal(parse_path("R75,D30,R83,U83,L12,D49,R71,U7,L72"),
                           parse_path("U62,R66,U55,R34,D71,R55,D58,R83")) == 610
    assert shortest_signal(parse_path("R98,U47,R26,D63,R33,U87,L62,D20,R33,U53,R51"),
                           parse_path("U98,R91,D20,R16,D67,R40,U7,R15,U6,R7")) == 410


def test_part1():
    assert part1() == 316


def test_part2():
    assert part2() == 16368
