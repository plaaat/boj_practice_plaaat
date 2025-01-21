use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n = input().parse::<usize>().unwrap();
    let inp1 = input();
    let nums = inp1.split_whitespace().map(|x| x.parse().unwrap()).collect::<Vec<i32>>();
    let mut dp = vec![vec![0;2]; n + 1];
    let mut max = nums[0];
    dp[0][0] = max;
    dp[0][1] = max;
    
    for i in 1..n {
        dp[i][0] = nums[i]; 
        dp[i][1] = nums[i];
        dp[i][0] = nums[i].max(dp[i-1][0] + nums[i]);
        dp[i][1] = dp[i-1][0].max(dp[i-1][1] + nums[i]);
        max = max.max(dp[i][0].max(dp[i][1]))
    }
    writeln!(res, "{}", max).unwrap();
    print!("{}", res);
}

// 제출번호 : 88372598, 메모리 : 19704, 시간 : 16 