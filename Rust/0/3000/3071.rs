use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let t = input().parse().unwrap();
    for _ in 0..t {
        let mut n:i64 = input().parse().unwrap();
        if n == 0 {
            writeln!(res,"0").unwrap();
            continue;
        }
        
        let flag = {if n < 0{false}else{true}};
        n = n.abs();
        let mut nli = vec![];
        while n > 0 {
            let nam = n % 3;
            if nam == 2 {
                nli.push(-1);
                n = (n + 1) / 3
            } else if nam == 1 {
                nli.push(1);
                n = (n - 1) / 3
            } else {
                nli.push(0);
                n = n / 3
            }
        }
        
        let mut out = String::new();
        if flag {
            for &i in nli.iter().rev() {
                if i == 1 {
                    out.push('1');
                } else if i == 0 {
                    out.push('0');
                } else {
                    out.push('-');
                }
            }
        } else {
            for &i in nli.iter().rev() {
                if i == 1 {
                    out.push('-');
                } else if i == 0 {
                    out.push('0');
                } else {
                    out.push('1');
                }
            }
        }
        writeln!(res,"{out}").unwrap()
    }
    print!("{res}")
}

// 제출 번호 : 90074065, 메모리 : 13212, 시간 : 0