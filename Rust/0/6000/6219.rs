use std::{
    fmt::Write,
    io::{self, BufRead}
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();

    let inp1 = input();
    let mut inp1 = inp1.split_whitespace();
    let (a,b,d): (i32,i32,i32) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );

    let mut primetf = vec![true; (b+1) as usize];
    primetf[0] = false;
    primetf[1] = false;
    
    let mut i = 2;
    while i * i <= b {
        if primetf[i as usize] {
            let mut j = i * i;
            while j <= b {
                primetf[j as usize] = false;
                j += i;
            }
        }
        i += 1;
    }
    
    let mut pli = vec![];
    for i in a..=b {
        if primetf[i as usize] {
            pli.push(i);
        }
    }
    let pn = pli.iter()
        .filter(|&&x| {
            let mut num = x;
            while num > 0 {
                if num % 10 == d {
                    return true;
                }
                num /= 10;
            }
            x == d
        })
        .count();
    writeln!(res, "{}", pn).unwrap();
    print!("{}", res);
}

// 제출 번호 : 86719300, 메모리 : 18144, 시간 : 20 
