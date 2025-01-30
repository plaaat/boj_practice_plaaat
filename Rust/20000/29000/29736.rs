use std::{
    fmt::Write,
    io::{self, BufRead},
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
    let inp2 = input();
    let inp1:Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let inp2:Vec<i32> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a,b,k,x):(i32,i32,i32,i32) = (inp1[0],inp1[1],inp2[0],inp2[1]);
    let vec = (a..=b).collect::<Vec<i32>>();
    let len = vec.len();
    let mut prlen = len.clone();
    for i in 0..len {
        if vec[i] < k - x {
            prlen -= 1
        } else if vec[i] > k + x{
            prlen -= len - i;
            break;
        }
    }
    if prlen <= 0 {
        writeln!(res,"IMPOSSIBLE").unwrap()
    } else {
        writeln!(res,"{}",prlen).unwrap()
    }

    print!("{}",res)
}



#  제출 번호 : 87847563, 메모리 : 13212, 시간 : 0