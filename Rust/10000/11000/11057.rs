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
    let n:i32 = input().parse().unwrap();
    let mut dp: Vec<i64> = vec![1;10];
    
    for _ in 1..n {
        for j in 1..10 {
            dp[j] += dp[j - 1] % 10007;
        }
    }
    
    let mut pn = 0;
    for i in 0..10 {
        pn += dp[i];
    }
    writeln!(res,"{}",pn % 10007).unwrap();
    print!("{}", res);
}

// 제출 번호 : 87273142, 메모리 : 13208, 시간 : 0
