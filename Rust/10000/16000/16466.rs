use std::io::{self, BufRead};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let n:i32 = input().parse().unwrap();
    let inp1 = input();
    let mut li:Vec<i32> = inp1
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();

    li.sort_unstable();
    let mut tf = false;
    for i in 1..=n {
        if li[(i - 1) as usize] != i {
            println!("{}",i);
            tf = true;
            break;
        }
    }
    if !tf {println!("{}",n+1)}
}


// 제출 번호 : 86452878, 메모리 : 28140, 시간 : 56