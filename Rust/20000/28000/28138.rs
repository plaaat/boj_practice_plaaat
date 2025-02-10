use std::{fmt::Write,io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1: Vec<i64> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n,r) = (inp1[0],inp1[1]);
    let mut ans = 0;
    let n = n-r;
    let mut i = 1;
    
    while i * i < n {
        if n % i != 0 {
            i += 1;
            continue;
        }
        if i > r {
            ans += i;
        }
        if n / i > r {
            ans += n / i;
        }
        i += 1;
    }

    if i * i == n && i > r {
        ans += i;
    }

    writeln!(res,"{ans}").unwrap();
    print!("{res}")
}

// 제출 번호 : 89410367, 메모리 : 13208, 시간 : 12