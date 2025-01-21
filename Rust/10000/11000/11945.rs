use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1 = inp1.split_whitespace().map(|x| x.parse().unwrap()).collect::<Vec<i32>>();
    let n= inp1[0];
    for _ in 0..n {
        let wo = input();
        writeln!(res, "{}", wo.chars().rev().collect::<String>()).unwrap();
    }
    print!("{}", res);
}

// 제출번호 : 88468327, 메모리 : 13212, 시간 : 0 