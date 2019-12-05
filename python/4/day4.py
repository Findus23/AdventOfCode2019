from collections import Counter

INPUT = "245182-790572"


def increasing_digit(number: int) -> bool:
    prev = 0
    for char in str(number):
        if prev > int(char):
            return False
        else:
            prev = int(char)
    return True


def has_adjacent_digits(number: int) -> bool:
    prev = None
    for char in str(number):
        if prev == char and prev is not None:
            return True
        else:
            prev = char
    return False


def has_adjacent_digits_that_arent_part_of_a_larger_group(number: int) -> bool:
    stats = Counter(str(number))
    for key, count in stats.items():
        if count == 2:
            return True
    return False


def part1() -> int:
    lower, upper = map(int, INPUT.split("-"))
    validcount = 0
    for pw in range(lower, upper + 1):
        if increasing_digit(pw) and has_adjacent_digits(pw):
            validcount += 1

    return validcount

def part2() -> int:
    lower, upper = map(int, INPUT.split("-"))
    validcount = 0
    for pw in range(lower, upper + 1):
        if increasing_digit(pw) and has_adjacent_digits_that_arent_part_of_a_larger_group(pw):
            validcount += 1

    return validcount


if __name__ == '__main__':
    print(part1())
    print(part2())
