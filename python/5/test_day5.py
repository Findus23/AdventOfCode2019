from day5 import run_intcode, decode_code, part1, part2

complex = [3, 21, 1008, 21, 8, 20, 1005, 20, 22, 107, 8, 21, 20, 1006, 20, 31,
           1106, 0, 36, 98, 0, 0, 1002, 21, 125, 20, 4, 20, 1105, 1, 46, 104,
           999, 1105, 1, 46, 1101, 1000, 1, 20, 4, 20, 1105, 1, 46, 98, 99]


def test_new_opcodes():
    assert run_intcode([3, 0, 4, 0, 99], input=33) == ([33, 0, 4, 0, 99], [33])


def test_parameter_mode():
    assert run_intcode([1002, 4, 3, 4, 33], input=None) == ([1002, 4, 3, 4, 99], [])


def test_negative_case():
    assert run_intcode([1101, 100, -1, 4, 0], input=42) == ([1101, 100, -1, 4, 99], [])


def test_decode_code():
    assert decode_code(1002) == (10, 2)


def test_part1():
    assert part1() == [0, 0, 0, 0, 0, 0, 0, 0, 0, 7286649]


def test_advanced1_false():
    assert run_intcode(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input=42) == ([3, 9, 8, 9, 10, 9, 4, 9, 99, 0, 8], [0])


def test_advanced1_true():
    assert run_intcode(
        [3, 9, 8, 9, 10, 9, 4, 9, 99, -1, 8], input=8) == ([3, 9, 8, 9, 10, 9, 4, 9, 99, 1, 8], [1])


def test_advanced2_false():
    assert run_intcode(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input=10) == ([3, 9, 7, 9, 10, 9, 4, 9, 99, 0, 8], [0])


def test_advanced2_true():
    assert run_intcode(
        [3, 9, 7, 9, 10, 9, 4, 9, 99, -1, 8], input=5) == ([3, 9, 7, 9, 10, 9, 4, 9, 99, 1, 8], [1])


def test_advanced3_false():
    assert run_intcode(
        [3, 3, 1108, -1, 8, 3, 4, 3, 99], input=10) == ([3, 3, 1108, 0, 8, 3, 4, 3, 99], [0])


def test_advanced3_true():
    assert run_intcode(
        [3, 3, 1108, -1, 8, 3, 4, 3, 99], input=8) == ([3, 3, 1108, 1, 8, 3, 4, 3, 99], [1])


def test_advanced4_false():
    assert run_intcode(
        [3, 3, 1107, -1, 8, 3, 4, 3, 99], input=10) == ([3, 3, 1107, 0, 8, 3, 4, 3, 99], [0])


def test_advanced4_true():
    assert run_intcode(
        [3, 3, 1107, -1, 8, 3, 4, 3, 99], input=5) == ([3, 3, 1107, 1, 8, 3, 4, 3, 99], [1])


def test_jump1_nonzero():
    assert run_intcode(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input=5)[1][0] == 1


def test_jump1_zero():
    assert run_intcode(
        [3, 12, 6, 12, 15, 1, 13, 14, 13, 4, 13, 99, -1, 0, 1, 9], input=0)[1][0] == 0


def test_jump2_nonzero():
    assert run_intcode(
        [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input=5)[1][0] == 1


def test_jump2_zero():
    assert run_intcode(
        [3, 3, 1105, -1, 9, 1101, 0, 0, 12, 4, 12, 99, 1], input=0)[1][0] == 0


def test_complex_below_8():
    assert run_intcode(complex, input=5)[1][0] == 999


def test_complex_8():
    assert run_intcode(complex, input=8)[1][0] == 1000


def test_complex_above_8():
    assert run_intcode(complex, input=15)[1][0] == 1001


def test_part2():
    assert part2() == [15724522]
