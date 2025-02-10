use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();
    let mut dp: Vec<i32> = vec![0; n as usize + 1];
    if n >= 2 {
        dp[2] = 2
    }

    for i in 3..n+1 {
        dp[i as usize] = (dp[i as usize - 1] * 3) % 1000000009
    }
    writeln!(res,"{}",dp[n as usize]).unwrap();
    print!("{res}")
}

// 제출 번호 : 89870716, 메모리 : 13472, 시간 : 0