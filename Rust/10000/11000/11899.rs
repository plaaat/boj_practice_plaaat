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
    let inp = input();
    let mut count = 0;
    let mut pn = 0;
    
    for c in inp.chars() {
        if c == '(' {
            count += 1;
        } else {
            if count == 0 {
                pn += 1;
            } else {
                count -= 1;
            }
        }
    }
    pn += count;
    
    writeln!(res, "{}", pn).unwrap();
    print!("{}", res);
} 

// 제출 번호 : 86994180, 메모리 : 13020, 시간 : 0ms