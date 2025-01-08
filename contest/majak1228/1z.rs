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
    let inp1 = input();
    let inp2 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let mut inp2 = inp2.split_ascii_whitespace();
    let (a,b):(i32,i32) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
        );
    let (c,d):(i32,i32) = (
        inp2.next().unwrap().parse().unwrap(),
        inp2.next().unwrap().parse().unwrap()
        );
    
    let mut now = 1;
    for _ in 1..a+b {
        now += 1;
        if now == 5 {
            now = 1
        }
    }
    for _ in 1..c+d {
        now += 1;
        if now == 5 {
            now = 1
        }
    }
    writeln!(res,"{}",now).unwrap();
    print!("{}", res);
}

// 제출 번호 : 87888374, 메모리 : 13396, 시간 : 0
