use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    loop {
        let inp = input();
        let mut inp = inp.split("C");
        let (r,mut c):(i32,i32) = (
            inp.next().unwrap()
            .strip_prefix("R").unwrap()
            .parse().unwrap(),
            inp.next().unwrap().parse().unwrap()
        );

        if r == 0 && c == 0 {
            break;
        }

        let mut tres = String::new();

        while c > 0 {
            c -= 1;
            tres.push((b'A' + (c % 26) as u8) as char);
            c /= 26;
        }

        tres = tres.chars().rev().collect();

        writeln!(res, "{}{}", tres, r).unwrap();
    }

    print!("{}", res);
}

// 제출 번호 : 86547506, 메모리 : 2757, 시간 : 0
