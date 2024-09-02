use std::io;

fn main() {
    let mut a = String::new();

    io::stdin().read_line(&mut a).expect("error");

    let a = a.trim();

    let mut part = a.split_whitespace();

    let x: u32 = part.next().unwrap_or("0").parse().expect("ddd");
    let y: u32 = part.next().unwrap_or("0").parse().expect("ddd");
    let sum = x+y;

    println!("{}", sum)
}
