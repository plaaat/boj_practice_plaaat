use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1: Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n, mut k) = (inp1[0], inp1[1]);
    let wo = input();
    let mut wo: Vec<u8> = wo.as_bytes().to_vec();
    let mut idx = 0;

    while k > 0 {
        if idx == n - 1 {
            k %= 26;
            if k > 'Z' as i32 + 1 - wo[idx as usize] as i32 {
                k -= 'Z' as i32 + 1 - wo[idx as usize] as i32;
                wo[idx as usize] = 'A' as u8;
            }
            wo[idx as usize] += k as u8;
            k = 0;
        } else {
            if wo[idx as usize] == 'A' as u8 {
                idx += 1;
            } else {
                let count = 'Z' as i32 - wo[idx as usize] as i32 + 1;
                if count <= k {
                    wo[idx as usize] = 'A' as u8;
                    k -= count;
                    idx += 1;
                } else {
                    idx += 1;
                }
            }
        }
    }

    let wo: String = wo.iter().map(|&x| x as char).collect();
    writeln!(res, "{}", wo).unwrap();
    print!("{}", res);
}



#  제출 번호 : 89117976, 메모리 : 14196, 시간 : 4