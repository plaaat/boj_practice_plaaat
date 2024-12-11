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
    let inp1 = input();
    let mut nli = inp1.split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());

    let mut pn = 0;
    for _ in 0..5 {
        let t = nli.next().unwrap();
        if t == n {
            pn += 1
        }
    }

    writeln!(res,"{}",pn).unwrap();
    print!("{}", res);
}

// 제출번호 : 87378489, 메모리 : 13208, 시간 : 0