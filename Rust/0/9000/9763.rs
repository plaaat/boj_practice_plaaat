use std::{fmt::Write, i32, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let t:i32 = input().parse().unwrap();
    let mut ma = Vec::with_capacity(t as usize);
    for _ in 0..t {
        let inp2 = input();
        let inp2:Vec<i32> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
        let tem = (inp2[0],inp2[1],inp2[2]);
        ma.push(tem);
    }

    let mut minn = i32::MAX;
    for i in 0..t {
        let mut m1 = i32::MAX;
        let mut m2 = i32::MAX;
        let ma1 = ma[i as usize];
        for j in 0..t {
            if i == j {continue;}
            let ma2 = ma[j as usize];
            let dis = (ma1.0 - ma2.0).abs() + (ma1.1 - ma2.1).abs() + (ma1.2 - ma2.2).abs();
            if m1 > dis {
                m2 = m1;
                m1 = dis
            } else if m2 > dis {
                m2 = dis
            }
        }
        minn = minn.min(m1 + m2)
    }
    writeln!(res,"{minn}").unwrap();
    print!("{res}")
}

// 제출 번호 : 89564737, 메모리 : 13208, 시간 : 416