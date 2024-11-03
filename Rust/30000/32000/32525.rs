use std::io::{self, BufRead};
use std::fmt::Write;

fn input() -> String {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    let t:i16 = input().parse().unwrap();
    for _ in 0..t {
        let n: i8 = input().parse().unwrap();
        for i in 1..=n {
            let inp = input();
            let mut inp = inp.split_ascii_whitespace();
            let (n, m) = (
                inp.next().unwrap().parse::<i64>().unwrap(),
                inp.next().unwrap().parse::<i32>().unwrap()
            );

            writeln!(output,"{} {} {}",i,n+50000000,m+1).unwrap()
        }
    }
    print!("{}",output);
}

// 제출번호 : 85942282, 메모리 : 17312, 시간 : 32