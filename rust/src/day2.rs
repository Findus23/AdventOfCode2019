use std::fs;

type IntCode = Vec<i32>;

fn parse_intcode(codestr: &str) -> IntCode {
    let split: IntCode = codestr
        .split(",")
        .map(|codestr| codestr.parse::<i32>().expect("can't parse intcode"))
        .collect();
    return split;
}

fn run_intcode(mut cl: IntCode) -> IntCode {
    let mut p = 0; // pointer,
    loop {
        let code = cl[p];
        if code == 99 {
            break;
        }
        let from1 = cl[p + 1] as usize;
        let from2 = cl[p + 2] as usize;
        let to = cl[p + 3] as usize;
        cl[to] = match code {
            1 => cl[from1] + cl[from2],
            2 => cl[from1] * cl[from2],
            _ => panic!("invalid intcode: {}", code),
        };
        p += 4
    }

    return cl;
}

pub fn part1() -> i32 {
    let mut data = fs::read_to_string("../python/2/input.txt").expect("Unable to read file");
    data.pop();
    let mut cl = parse_intcode(data.as_str());
    cl[1] = 12;
    cl[2] = 2;

    cl = run_intcode(cl);
    return cl[0];
}
pub fn part2() -> i32 {
    let mut data = fs::read_to_string("../python/2/input.txt").expect("Unable to read file");
    data.pop();
    let inital_cl = parse_intcode(data.as_str());
    let mut cl: IntCode;
    for noun in 0..99 {
        for verb in 0..99 {
            cl = inital_cl.clone();
            cl[1] = noun;
            cl[2] = verb;
            cl = run_intcode(cl);
            if cl[0] == 19690720 {
                return 100 * noun + verb;
            }
        }
    }
    return -1;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_parse_intcode() {
        assert_eq!(parse_intcode("2,2,3,45,5"), [2, 2, 3, 45, 5])
    }
    #[test]
    #[should_panic(expected = "invalid intcode: 123")]
    fn test_opcode_panics() {
        let cl = vec![123, 123, 123, 123];
        run_intcode(cl);
    }
    #[test]
    fn test_run_intcode1() {
        let mut cl: IntCode = vec![1, 0, 0, 0, 99];
        cl = run_intcode(cl);
        assert_eq!(cl, vec![2, 0, 0, 0, 99])
    }
    #[test]
    fn test_run_intcode2() {
        let mut cl: IntCode = vec![2, 3, 0, 3, 99];
        cl = run_intcode(cl);
        assert_eq!(cl, vec![2, 3, 0, 6, 99])
    }
    #[test]
    fn test_run_intcode3() {
        let mut cl: IntCode = vec![2, 4, 4, 5, 99, 0];
        cl = run_intcode(cl);
        assert_eq!(cl, vec![2, 4, 4, 5, 99, 9801])
    }
    #[test]
    fn test_run_intcode4() {
        let mut cl: IntCode = vec![1, 1, 1, 4, 99, 5, 6, 0, 99];
        cl = run_intcode(cl);
        assert_eq!(cl, vec![30, 1, 1, 4, 2, 5, 6, 0, 99])
    }
    #[test]
    fn test_part1() {
        assert_eq!(part1(), 4714701)
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(), 5121)
    }
}
