use std::{collections::VecDeque, io::{self, BufRead}};

fn input() -> String {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let inp = input();
    let mut iter = inp.split_ascii_whitespace();
    let (mut n, k) = (
        iter.next().unwrap().parse::<i32>().unwrap(),
        iter.next().unwrap().parse::<i32>().unwrap()
    );
    
    let mut now = VecDeque::with_capacity(n as usize);
    now.extend(1..=n);
    
    let mut fir = now.pop_front().unwrap();
    now.push_back(fir);
    
    while n != 1 {
        for _ in 1..k {
            if n == 1 {
                println!("{}", fir);
                return;
            }
            n -= 1;
            now.pop_front();
        }
        
        if n == 1 {
            println!("{}", now.pop_front().unwrap());
            return;
        }
        
        fir = now.pop_front().unwrap();
        now.push_back(fir);
    }
}

// 제출번호 : 85935777, 메모리 : 17116, 시간 : 8