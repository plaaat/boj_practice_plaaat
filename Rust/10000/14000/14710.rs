use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1:Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (h,m) = (inp1[0], inp1[1]);
    if (h % 30) * 12 == m {
        writeln!(res,"O").unwrap()
    } else {
        writeln!{res,"X"}.unwrap()
    }
    print!("{}", res);
}

// 제출번호 : 89071068, 메모리 : 13208, 시간 : 0 