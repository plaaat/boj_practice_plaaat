use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let mut res = String::new();
    let mut n = input().parse::<i32>().unwrap();
    n %= 2;
    if n == 0 {
        writeln!(res, "CY").unwrap();
    } else {
        writeln!(res, "SK").unwrap();
    }
    print!("{}", res);
}

// 제출번호 : 88599758, 메모리 : 13208, 시간 : 4 