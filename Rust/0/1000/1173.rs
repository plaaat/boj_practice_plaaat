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
    let (n,m,mm,t,r) = (inp1[0],inp1[1],inp1[2],inp1[3],inp1[4]);
    let mut time = 0;
    let mut count = 0;
    let mut hp = 0;
    hp += m;
    if hp + t > mm {
        println!("-1");
        return;
    }
    while count < n {
        time += 1;
        if hp + t <= mm && hp + t >= m {
            hp += t;
            count += 1;
        } else if hp - r < m {
            hp = m;
        } else {
            hp -= r;
        }
    }
    writeln!(res, "{}", time).unwrap();
    print!("{}", res);
}

// 제출 번호 : 88050053, 메모리 : 13208, 시간 : 0