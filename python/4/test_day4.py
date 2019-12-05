from day4 import increasing_digit, has_adjacent_digits, part1, has_adjacent_digits_that_arent_part_of_a_larger_group, \
    part2


def test_increasing_digit():
    assert increasing_digit(1234567)
    assert not increasing_digit(1236567)
    assert increasing_digit(1234447)


def test_has_adjacent_digits():
    assert has_adjacent_digits(11345345)
    assert has_adjacent_digits(343244)
    assert not has_adjacent_digits(2454367)


def test_example_codes():
    assert has_adjacent_digits(111111) and increasing_digit(111111)
    assert has_adjacent_digits(223450) and not increasing_digit(223450)
    assert not has_adjacent_digits(123789) and increasing_digit(123789)


def test_has_adjacent_digits_that_arent_part_of_a_larger_group():
    assert has_adjacent_digits_that_arent_part_of_a_larger_group(11345345)
    assert has_adjacent_digits_that_arent_part_of_a_larger_group(343244)
    assert not has_adjacent_digits_that_arent_part_of_a_larger_group(24544467)


def test_more_example_codes():
    assert has_adjacent_digits_that_arent_part_of_a_larger_group(112233)
    assert not has_adjacent_digits_that_arent_part_of_a_larger_group(123444)
    assert has_adjacent_digits_that_arent_part_of_a_larger_group(111122)


def test_part1():
    assert part1() == 1099


def test_part2():
    assert part2() == 710
