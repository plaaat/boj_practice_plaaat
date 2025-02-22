use std::{fmt::Write, i32, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();
    let cross:Vec<i32> = input().split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let lft:Vec<i32> = input().split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let rgt:Vec<i32> = input().split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    
    let mut lfts = vec![0;n as usize + 1];
    let mut rgts = vec![0;n as usize + 1];
    let mut minn = i64::MAX;
    let mut cres = i32::MAX;
    for i in 1..n as usize {
        lfts[i] = lfts[i - 1] + lft[i - 1] as i64;
        rgts[n as usize - i] = rgts[n as usize - i + 1] + rgt[n as usize - i - 1] as i64
    }

    for i in 1..n+1 {
        let sumn = cross[i as usize - 1] as i64 + lfts[i as usize - 1] + rgts[i as usize];
        if sumn < minn {
            minn = sumn;
            cres = i
        }
    }
    writeln!(res,"{cres} {minn}").unwrap();
    print!("{res}")
}

// 제출 번호 : 90113556, 메모리 : 16468, 시간 : 12