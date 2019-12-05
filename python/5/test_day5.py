from day5 import run_intcode, decode_code, part1


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
