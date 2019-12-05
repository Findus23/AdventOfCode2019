use std::env;

mod day1;
mod day2;

fn main() {
    let args: Vec<String> = env::args().collect();
    if args.len() < 2 {
        println!("specify day");
        std::process::exit(1);
    }
    let res1 = match args[1].as_str() {
        "1" => day1::part1(),
        "2" => day2::part1(),
        _ => -1,
    };
    let res2 = match args[1].as_str() {
        "1" => day1::part2(),
        "2" => day2::part2(),
        _ => -1,
    };

    println!("part 1: {}", res1);
    println!("part 1: {}", res2);
}
