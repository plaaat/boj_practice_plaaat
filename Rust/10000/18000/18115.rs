use std::{collections::VecDeque, io::{self,BufRead}};

fn read_line() -> String {
    let mut line = String::new();
    io::stdin().lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let n : usize = read_line().parse().unwrap();
    let li : Vec<i32> = read_line()
        .split_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let nli : Vec<usize> = (1..=n).collect();
    let mut q : VecDeque<usize> = VecDeque::new();
    
    for i in 0..n {
        if li[n - i - 1] == 1 {
            q.push_front(nli[i]);
        } else if li[n - i - 1] == 2 {
            let t : usize = q.pop_front().unwrap();
            q.push_front(nli[i]);
            q.push_front(t);
        } else {
            q.push_back(nli[i]);
        }
    }
    println!("{}",q.iter()
                    .map(|&x|x.to_string())
                    .collect::<Vec<String>>()
                    .join(" "));
}

// 제출 번호 : 85770198, 메모리 : 94740, 시간 : 152
