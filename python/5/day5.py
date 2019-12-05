from typing import List, Tuple

intcode = List[int]
INPUT = 1


def parse_intcode(text: str) -> intcode:
    return list(map(int, text.split(",")))


def decode_code(code: int):
    paramcode, opcode = divmod(code, 100)  # splits 12345 into (123,45)
    return paramcode, opcode


class ParamReader():
    def __init__(self, pointer, cl, paramcode):
        self.pointer = pointer
        self.cl = cl
        self.paramcode = paramcode

    def index(self, id):
        return self.cl[self.pointer + id]

    def param(self, id):
        param_mode = (self.paramcode // 10 ** (id - 1)) % 10
        if param_mode == 1:
            return self.index(id)
        elif param_mode == 0:
            return self.cl[self.index(id)% len(self.cl)]
        else:
            raise ValueError(f"invalid parameter code {param_mode} for parameter {id}")


def run_intcode(codelist: intcode, input) -> Tuple[intcode, List[int]]:
    # codelist.extend([99, 99, 99])  # hack so we don't look over the edge
    output = []
    p = 0  # pointer
    while True:
        paramcode, code = decode_code(codelist[p])
        pr = ParamReader(p, codelist, paramcode)

        if code == 99:
            break
        if code == 1:
            codelist[pr.index(3)] = pr.param(1) + pr.param(2)
        elif code == 2:
            codelist[pr.index(3)] = pr.param(1) * pr.param(2)
        elif code == 3:
            codelist[pr.index(1)] = input
        elif code == 4:
            output.append(pr.param(1))
        elif code == 5:  # jump if true
            if pr.param(1):
                p = pr.param(2)
            else:
                p += 3
        elif code == 6:  # jump if false
            if not pr.param(1):
                p = pr.param(2)
            else:
                p += 3
        elif code == 7:  # less than
            codelist[pr.index(3)] = 1 if (pr.param(1) < pr.param(2)) else 0
        elif code == 8:  # equals
            codelist[pr.index(3)] = 1 if (pr.param(1) == pr.param(2)) else 0
        else:
            raise ValueError(f"invalid intcode: {code}")
        if code in [1, 2,7, 8]:
            p += 4
        elif code in [3, 4]:
            p += 2
    return codelist, output


def part1() -> List[int]:
    with open("5/input.txt") as f:
        cl = parse_intcode(f.read())
    cl, output = run_intcode(cl, input=1)

    return output


def part2() -> List[int]:
    with open("5/input.txt") as f:
        cl = parse_intcode(f.read())
    cl, output = run_intcode(cl, input=5)

    return output


if __name__ == '__main__':
    # print(part1())
    print(part2())
