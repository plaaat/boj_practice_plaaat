use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    let n: usize = input().parse().unwrap();
    let inp1 = input();
    let li:Vec<i64> = inp1
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut dp = vec![1;n];
    let mut pn = 1;
    for i in 1..n {
        for j in 0..i {
            if li[i] < li[j] {
                dp[i] = dp[i].max(dp[j]+1)
            }
        }
        pn = pn.max(dp[i]);
    }
    
    writeln!(output,"{}",n - pn as usize).unwrap();
    print!("{}",output);
}

// 제출 번호 : 86218923, 메모리 : 13216, 시간 : 8