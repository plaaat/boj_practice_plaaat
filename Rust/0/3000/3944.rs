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
    let t: usize = input().parse().unwrap();

    for _ in 0..t {
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace();
        let n: u32 = inp1.next().unwrap().parse().unwrap();

        if n == 2 {
            writeln!(res, "0").unwrap();
            continue;
        }

        let wo = inp1.next().unwrap();
        let mut pn = 0;
        for i in wo.chars() {
            let t = i.to_digit(n).unwrap();
            pn = (pn * n + t) % (n - 1)
        }
        writeln!(res, "{}", pn).unwrap();
    }

    print!("{}", res);
}

// 제출번호 : 87398517, 메모리 : 34288, 시간 : 484