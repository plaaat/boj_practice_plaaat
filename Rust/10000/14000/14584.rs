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

    let wo = input();
    let n = input().parse().unwrap();
    let mut lis = vec![];
    for _ in 0..n {
        let inp1 = input();
        lis.push(inp1);
    }
    for i in 0..26 {
        let mut two = vec![];
        for j in 0..wo.len() {
            two.push(((wo.as_bytes()[j] - b'a' + i as u8 + 1) % 26 + b'a') as char);
        }
        let two = two.iter().collect::<String>();
        for ttw in lis.iter() {
            if two.contains(ttw) {
                writeln!(res, "{}", two).unwrap();
                break;
            }
        }
    }

    print!("{}", res);
}

// 제출 번호 : 86713971, 메모리 : 13212, 시간 : 0 
