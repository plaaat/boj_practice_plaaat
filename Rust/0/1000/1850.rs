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

fn gcd(a: i64, b: i64) -> usize {
    if b == 0 {
        a as usize
    } else {
        gcd(b, a % b)
    }
}


fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace()
        .map(|x| x.parse::<i64>().unwrap());
    let (a, b) = (
        inp1.next().unwrap(),
        inp1.next().unwrap(),
    );

    writeln!(res, "{}", "1".repeat(gcd(a,b))).unwrap();
    print!("{}", res);
}

// 제출번호 : 87306218, 메모리 : 27860, 시간 : 8