use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn gcd(a: i64, b: i64) -> i64 {
    if b == 0 {
        return a;
    }
    gcd(b, a % b)
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1: Vec<i64> = inp1.split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n,m) = (inp1[0],inp1[1]);
    
    let mut drinks = Vec::with_capacity(n as usize);
    for _ in 0..n {
        let inp2 = input();
        let inp2: Vec<i64> = inp2.split_whitespace().map(|x| x.parse().unwrap()).collect();
        drinks.push((inp2[1],inp2[0]));
    }

    drinks.sort_unstable_by(|a,b| 
        (a.0 * b.1).cmp(&(b.0 * a.1))
    );

    let mut drink = 0;
    let mut sumo = 1;
    let mut suja = 0;
    
    while drink < m {
        let (v,w) = drinks.pop().unwrap();
        if drink + w <= m {
            drink += w;
            suja += v;
        } else {
            let a = m - drink;
            (suja,sumo) = (suja * w + sumo * v * a, sumo * w);
            drink = m;
        }
    }
    
    let gcd = gcd(suja,sumo);
    writeln!(res,"{}/{}",suja/gcd,sumo/gcd).unwrap();

    print!("{}", res);
}

// 제출번호 : 88371328, 메모리 : 14780, 시간 : 36 