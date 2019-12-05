def calculate_fuel(mass: int) -> int:
    return mass // 3 - 2


def part1() -> int:
    total = 0

    with open("1/input.txt") as f:
        for line in f:
            m = int(line)
            fuel = calculate_fuel(m)
            total += fuel
    return total


def advanced_fuel(mass: int) -> int:
    total = 0
    while True:
        fuel = calculate_fuel(mass)
        if fuel > 0:
            total += fuel
            mass = fuel
        else:
            break
    return total


def part2() -> int:
    total = 0

    with open("1/input.txt") as f:
        for line in f:
            m = int(line)
            fuel = advanced_fuel(m)
            total += fuel
    return total


if __name__ == '__main__':
    print(part1())
    print(part2())
