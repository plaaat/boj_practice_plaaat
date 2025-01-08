use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let mut res = String::new();
    let wo1 = input().bytes().collect::<Vec<u8>>();
    let wo2 = input().bytes().collect::<Vec<u8>>();
    
    let mut dp = vec![vec![0;wo2.len() + 1];wo1.len() + 1];
    let mut maxl = 0;
    

    for i in 1..=wo1.len() {
        for j in 1..=wo2.len() {
            if wo1[i-1] == wo2[j-1] {
                dp[i][j] = dp[i-1][j-1] + 1;
                if dp[i][j] > maxl {
                    maxl = dp[i][j];
                }
            } else {
                dp[i][j] = 0;
            }
        }
    }
    writeln!(res, "{}", maxl).unwrap();
    print!("{}", res);
}

// 제출 번호 : 88170426, 메모리 : 75848, 시간 : 104