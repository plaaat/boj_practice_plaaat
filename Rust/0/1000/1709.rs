use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let mut res = String::new();
    let n = input().parse::<i64>().unwrap() / 2;
    let mut x = 0;
    let mut y = n - 1;
    let dis = (n).pow(2);
    let mut ans = 0;

    while x <= n && y >= 0 {
        let now = (x+1).pow(2) + y.pow(2);
        if now <= dis {
            x += 1;
        }
        if now >= dis {
            y -= 1;
        }
        ans += 1;
    }
    writeln!(res, "{}", ans * 4).unwrap();
    print!("{}", res);
}

// 제출번호 : 88518881, 메모리 : 13208, 시간 : 384 