use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    let t:i32 = input().parse().unwrap();
    
    for _ in 0..t {    
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace();
        let (n,k):(i32,i32) = (
            inp1.next().unwrap().parse().unwrap(),
            inp1.next().unwrap().parse().unwrap()
        );
        let mut pn = 0;
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();

        for _ in 0..n {
            let x:i32 = inp2.next().unwrap().parse().unwrap();
            pn += x/k;
        };
        writeln!(output,"{}",pn).unwrap();
    }    
    print!("{}",output);
}

// 제출 번호 : 86095494, 메모리 : 13208, 시간 : 0