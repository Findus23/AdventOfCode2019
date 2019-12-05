from typing import List

intcode = List[int]


def parse_intcode(text: str) -> intcode:
    return list(map(int, text.split(",")))


def run_intcode(codelist: intcode) -> intcode:
    p = 0  # pointer
    while True:
        code = codelist[p]
        if code == 99:
            break
        from1 = codelist[p + 1]
        from2 = codelist[p + 2]
        to = codelist[p + 3]
        if code == 1:
            codelist[to] = codelist[from1] + codelist[from2]
        elif code == 2:
            codelist[to] = codelist[from1] * codelist[from2]
        else:
            raise ValueError(f"invalid intcode: {code}")
        p += 4
    return codelist


def part1() -> int:
    with open("2/input.txt") as f:
        cl = parse_intcode(f.read())
    cl[1] = 12
    cl[2] = 2
    cl = run_intcode(cl)

    return cl[0]


def part2() -> int:
    with open("2/input.txt") as f:
        initial_cl = parse_intcode(f.read())

    for noun in range(99):
        for verb in range(99):
            cl = initial_cl[:]  # make a copy
            cl[1] = noun
            cl[2] = verb
            cl = run_intcode(cl)
            if cl[0] == 19690720:
                return 100 * noun + verb

    return -1


if __name__ == '__main__':
    print(part1())
    print(part2())
