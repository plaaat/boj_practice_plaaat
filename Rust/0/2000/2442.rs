use std::{
    fmt::Write,
    io::{self, BufRead}
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();

    for i in 1..=n {
        write!(res,"{}"," ".repeat((n - i) as usize)).unwrap();
        writeln!(res,"{}","*".repeat((2 * i - 1) as usize)).unwrap();
    }
    print!("{}",res)
}

// 제출번호 : 87563421, 메모리 : 13208, 시간 : 0