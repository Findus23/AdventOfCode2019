from day2 import opcode_parse, run_intcode, part1, part2


def test_opcode_parse():
    assert opcode_parse("2,2,3,45,5") == [2, 2, 3, 45, 5]


def test_run_intcode():
    assert run_intcode([1, 0, 0, 0, 99]) == [2, 0, 0, 0, 99]
    assert run_intcode([2, 3, 0, 3, 99]) == [2, 3, 0, 6, 99]
    assert run_intcode([2, 4, 4, 5, 99, 0]) == [2, 4, 4, 5, 99, 9801]
    assert run_intcode([1, 1, 1, 4, 99, 5, 6, 0, 99]) == [30, 1, 1, 4, 2, 5, 6, 0, 99]


def test_part1():
    assert part1() == 4714701


def test_part2():
    assert part2() == 5121
