use std::{
    fmt::Write,
    io::{self, BufRead},
    collections::VecDeque
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
    let inp1:Vec<i32> = inp1.split_ascii_whitespace()
        .map(|x| x.parse().unwrap()).collect();
    let (_,w,l) = (inp1[0],inp1[1],inp1[2]);
    
    let inp2 = input();
    let mut cars:VecDeque<i32> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let mut q = VecDeque::with_capacity(w as usize);
    let mut we = cars.pop_front().unwrap();
    let mut time = 1;
    q.push_back((we,0));
    
    while !q.is_empty() {
        for _ in 0..q.len() {
            let f = q.pop_front().unwrap();
            q.push_back((f.0,f.1 + 1));
        }

        if let Some(front) = q.pop_front() {
            if front.1 == w {
                we -= front.0;
            } else {
                q.push_front(front);
            }
        }

        if let Some(fcar) = cars.pop_front() {
            if fcar + we > l {
                cars.push_front(fcar);
            } else {
                we += fcar;
                q.push_back((fcar,0));
            }
        }
        time += 1
        
    }

    writeln!(res,"{}",time).unwrap();
    print!("{}", res)
}

// 제출 번호 : 87616389, 메모리 : 13212, 시간 : 0
