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
    let n = input().parse::<i64>().unwrap();
    let bn = format!("{:b}", n);
    
    let v_bn = bn.chars().collect::<Vec<char>>();
    let mut pn = 0;
    let lv = v_bn.len();
    
    for (i, j) in v_bn.iter().enumerate() {
        if j == &'1' {
            pn += 3_i64.pow((lv - i - 1) as u32);
        }
    }

    writeln!(res, "{}", pn).unwrap();
    print!("{}", res);
} 

// 제출 번호 : 86995408, 메모리 : 13212, 시간 : 0ms