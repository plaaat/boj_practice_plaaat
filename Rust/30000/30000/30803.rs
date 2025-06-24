use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();
    let inp2 = input();
    let mut ali: Vec<i64> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let q:i32 = input().parse().unwrap();
    let mut fla = vec![true;n as usize];
    let mut ans = ali.iter().sum::<i64>();
    writeln!(res,"{}",ans).unwrap();
    
    for _ in 0..q {
        let inp3 = input();
        let mut inp3 = inp3.split_ascii_whitespace();
        let x = inp3.next().unwrap();
        let a = inp3.next().unwrap().parse::<usize>().unwrap() - 1;
        if x == "1" {
            let b:i64 = inp3.next().unwrap().parse().unwrap();
            if fla[a] {
                ans -= ali[a];
                ans += b
            }
            ali[a] = b
        } else {
            if fla[a] {
                fla[a] = false;
                ans -= ali[a]
            } else {
                fla[a] = true;
                ans += ali[a]
            }
        }
        writeln!(res,"{}",ans).unwrap();
    }
    print!("{res}")
}

// 제출 번호 : 95623271, 메모리 : 24120, 시간 : 68