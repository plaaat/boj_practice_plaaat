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

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_whitespace()
        .map(|s| s.parse::<i32>().unwrap());
    let bw = inp1.next().unwrap();
    let bi = inp1.next().unwrap();
    let bt = inp1.next().unwrap();
    
    let inp2 = input();
    let mut inp2 = inp2.split_whitespace()
        .map(|s| s.parse::<i32>().unwrap());
    let d = inp2.next().unwrap();
    let i = inp2.next().unwrap();
    let a = inp2.next().unwrap();
    
    let (mut pw1, mut pw2) = (bw, bw);
    let mut pi = bi.clone();
    
    for _ in 0..d {
        pw1 += i - bi - a;
        pw2 += i - pi - a;
        
        if (i - (pi + a)).abs() > bt {
            pi += (i - (pi + a)) / 2;
        }
    }

    if pw1 <= 0 {
        writeln!(res, "Danger Diet").unwrap();
    }
    else {
        writeln!(res, "{} {}", pw1, bi).unwrap();
    }

    if pw2 <= 0 || pi <= 0 {
        writeln!(res, "Danger Diet").unwrap();
    }
    else {
        write!(res, "{} {}", pw2, pi).unwrap();
        if bi > pi {
            writeln!(res, " YOYO").unwrap();
        } else {
            writeln!(res, " NO").unwrap();
        }
    }
    print!("{}", res);
} 

// 틀렸습니다!!