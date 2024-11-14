use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (l,r) = (
        inp1.next().unwrap(),
        inp1.next().unwrap()
    );
    let mut pn = 0;
    if l.to_string().len() == r.to_string().len() {
        for i in 0..l.len() {
            if &l[i..i+1] == &r[i..i+1]{
                if &l[i..i+1] == "8" {
                    pn += 1
                }
            } else {
                break;
            }
        }
    }
    writeln!(output,"{}",pn).unwrap();
    print!("{}",output);
}

// 제출 번호 : 86229252, 메모리 : 13208, 시간 : 8