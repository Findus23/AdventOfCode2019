from day1 import calculate_fuel, part1, advanced_fuel, part2


def test_calculate_fuel():
    assert calculate_fuel(12) == 2
    assert calculate_fuel(14) == 2
    assert calculate_fuel(1969) == 654
    assert calculate_fuel(100756) == 33583


def test_part1():
    assert part1() == 3226488


def test_advanced_fuel():
    assert advanced_fuel(14) == 2
    assert advanced_fuel(1969) == 966
    assert advanced_fuel(100756) == 50346

def test_part2():
    assert part2()==4836845
