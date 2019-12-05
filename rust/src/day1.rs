use std::fs;

fn calculate_fuel(mass: i32) -> i32 {
    return mass / 3 - 2;
}

fn advanced_fuel(mass: i32) -> i32 {
    let mut mass = mass;
    let mut total = 0;
    let mut fuel;
    loop {
        fuel = calculate_fuel(mass);
        if fuel > 0 {
            total += fuel;
            mass = fuel;
        } else {
            break;
        }
    }
    return total;
}

pub fn part1() -> i32 {
    let data = fs::read_to_string("../python/1/input.txt").expect("Unable to read file");
    let ints = data
        .lines()
        .map(|line| calculate_fuel(line.parse().expect("error when parsing line as integer")))
        .sum();
    return ints;
}

pub fn part2() -> i32 {
    let data = fs::read_to_string("../python/1/input.txt").expect("Unable to read file");
    let ints = data
        .lines()
        .map(|line| advanced_fuel(line.parse().expect("error when parsing line as integer")))
        .sum();
    return ints;
}

#[cfg(test)]
mod tests {
    use super::*;
    #[test]
    fn test_calculate_fuel() {
        assert_eq!(calculate_fuel(12), 2);
        assert_eq!(calculate_fuel(14), 2);
        assert_eq!(calculate_fuel(1969), 654);
        assert_eq!(calculate_fuel(100756), 33583);
    }

    #[test]
    fn test_advanced_fuel() {
        assert_eq!(advanced_fuel(14), 2);
        assert_eq!(advanced_fuel(1969), 966);
        assert_eq!(advanced_fuel(100756), 50346);
    }

    #[test]
    fn test_part1() {
        assert_eq!(part1(), 3226488)
    }

    #[test]
    fn test_part2() {
        assert_eq!(part2(), 4836845)
    }
}
