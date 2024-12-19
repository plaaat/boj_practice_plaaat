use std::
    io::{self, BufRead}
;

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let n:i32 = input().parse().unwrap();
    let mut ang = 180 * (n-2);
    let inp2 = input();
    let mut inp2 = inp2.split_ascii_whitespace();
    
    for _ in 0..n {
        let x:i32 = inp2.next().unwrap().parse().unwrap();
        ang -= x * 2
    }
    print!("{}",ang + 180)
}

// 제출번호 : 87577213, 메모리 : 13208, 시간 : 0
//... 왜맞앗지..?