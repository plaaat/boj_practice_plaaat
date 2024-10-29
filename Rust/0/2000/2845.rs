use std::io::{self,BufRead};

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let inp: Vec<i64> = read_line()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let a: i64 = inp[0];
    let b: i64 = inp[1];

    let li: Vec<i64> = read_line()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    println!("{}", li.iter()
        .map(|&x| (x - a * b).to_string())
        .collect::<Vec<String>>()
        .join(" "));
}

// 제출 번호 : 85734461, 메모리 : 13212, 시간 : 0