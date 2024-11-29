use std::{
    fmt::Write,
    io::{self, BufRead},
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
    let mut inp1 = inp1.split_whitespace()
        .map(|s| s.parse::<i32>().unwrap());
    let n = inp1.next().unwrap();
    let m = inp1.next().unwrap();
    let mut rooms = vec![0; n as usize + 1];
    for _ in 0..m {
        let inp2 = input();
        let mut inp2 = inp2.split_whitespace()
            .map(|s| s.parse().unwrap());
        let a = inp2.next().unwrap();
        let b = inp2.next().unwrap();
        let c = inp2.next().unwrap();
        let mut flag = true;
        if rooms[a as usize] > b {
            flag = false;
        } else {
            rooms[a as usize] = c;
        }
        if flag {
            writeln!(res, "YES").unwrap();
        } else {
            writeln!(res, "NO").unwrap();
        }
    }
    print!("{}", res);
} 

// 제출 번호 : 86965880, 메모리 : 15020, 시간 : 68 