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

    let n: usize = input().parse().unwrap();
    let inp1 = input();
    let li: Vec<i32> = inp1
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    let mut dp = vec![1;n];
    for i in 1..n {
        for j in 0..i {
            if li[j] < li[i] {
                dp[i] = dp[i].max(dp[j] + 1);
            }
        }
    }

    let mut mn = *dp.iter().max().unwrap();
    writeln!(res, "{}", mn).unwrap();
    let mut pli = vec![];
    for i in 0..n {
        if dp[n - i - 1] == mn {
            pli.push(li[n - i - 1]);
            mn -= 1;
        }
    }
    pli.reverse();
    writeln!(res, "{}", pli.iter()
        .map(|x| x.to_string())
        .collect::<Vec<String>>()
        .join(" ")
    ).unwrap();
    print!("{}", res);
}

// 제출 번호 : 86547506, 메모리 : 13216, 시간 : 4 
