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
    let (_,t) = (inp1[0],inp1[1]);
    let inp2 = input();
    let nli = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect::<Vec<i32>>();
    let mut ans = 0;
    for i in nli {
        let mut na = 0;
        while t % (i + na) != 0 && t % (i - na) != 0 {
            na += 1
        }
        ans += na
    }
    writeln!(res,"{}",ans).unwrap();
    print!("{}", res);
}

// 제출번호 : 89254543, 메모리 : 13212, 시간 : 8 