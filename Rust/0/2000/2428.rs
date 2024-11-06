use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    let t: usize = input().parse().unwrap();
    let li = input();
    let mut li: Vec<i64> = 
            li.split_ascii_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
    li.sort_unstable();

    let mut pn:usize = 0;
    for i in 0..t-1 {
        let mut left = i+1;
        let mut right = t;

        while left < right {
            let middle = left + (right-left)/2;
            if li[middle] * 9 <= li[i] * 10 {
                left = middle + 1;
            } else {
                right = middle;
            }
        }
        pn += left - (i + 1); 
    }
    writeln!(output,"{}",pn).unwrap();
    print!("{}",output);
}

// 제출 번호 : 86113089, 메모리 : 15512, 시간 : 16