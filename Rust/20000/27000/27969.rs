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
    let mut pn = 0;
    let wo = input();
    let mut intflag = false;
    let mut strlen = 0;

    for w in wo.chars() {
        if w == '['{
            pn += 8
        } else if w == ' ' {
            if intflag {
                intflag = false;
                pn += 8
            } else if strlen > 0 {
                pn += strlen + 12;
                strlen = 0
            }
        } else if w == ']'{
            continue;
        } else {
            let bitw = w as u8;
            if bitw >= b'1' && bitw <= b'9' {
                if !intflag {
                    intflag = true
                }
            } else if w.is_alphabetic() {
                strlen += 1
            }
        }
    }
    writeln!(res,"{}",pn).unwrap();
    print!("{}",res)
}

// 제출번호 : 87397681, 메모리 : 13208, 시간 : 0