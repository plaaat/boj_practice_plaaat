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
    let n = input().parse().unwrap();
    let mut dp = vec![false;n];
    dp[1] = true;
    for i in 3..n{
        if !dp[i - 1] || !dp[i - 3] {
            dp[i] = true;
        } else {
            dp[i] = false;
        }
    }
    if dp[n-1] {
        writeln!(res,"SK").unwrap();
    } else {
        writeln!(res,"CY").unwrap();
    }
    print!("{}",res)
}

// 제출 번호 : 87173703, 메모리 : 13208, 시간 : 4
