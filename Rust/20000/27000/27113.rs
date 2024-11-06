use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn max(a:i64,b:i64) -> i64 {
    if a > b {a}
    else {b}
}

fn min(a:i64,b:i64) -> i64 {
    if a < b {a}
    else {b}
}

fn main() {
    let mut output = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n,m) : (i32,i64) = 
        (inp1.next().unwrap().parse().unwrap(),
         inp1.next().unwrap().parse().unwrap());
    let mut tf = true;
    let mut now = 1;
    
    for _ in 1..n {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let sens:i32 = inp2.next().unwrap().parse().unwrap();
        
        if sens == 0 {
            continue;
        } else if sens == 1 {
            let (sen1,sen1d) : (i64,&str) = 
                (inp2.next().unwrap().parse().unwrap(),
                 inp2.next().unwrap(),);
            if sen1d == "R" {
                if now > sen1 - 1 {
                    tf = false;
                    break;
                }
            } else if sen1d == "L" {
                if sen1 == m {
                    tf = false;
                    break;
                }
                now = max(now, sen1 + 1);
            }
        } else {
            let (sen1,sen1d) : (i64,&str) = 
                (inp2.next().unwrap().parse().unwrap(),
                 inp2.next().unwrap(),);
            let (sen2,sen2d) : (i64,&str) = 
                (inp2.next().unwrap().parse().unwrap(),
                 inp2.next().unwrap(),);
                 
            if sen1d == sen2d {
                if sen1d == "R" {
                    let start = min(sen1, sen2);
                    if now > start - 1 {
                        tf = false;
                        break;
                    }
                } else {
                    let start = max(sen1, sen2);
                    if start == m {
                        tf = false;
                        break;
                    }
                    now = max(now, start + 1);
                }
            } else {
                let (mut sen1, mut sen2) = (sen1, sen2);
                if sen1d == "L" && sen2d == "R" {
                    std::mem::swap(&mut sen1, &mut sen2);
                }
                
                if sen1 <= sen2 {
                    if now >= sen1 {
                        if sen2 == m {
                            tf = false;
                            break;
                        }
                        now = max(now, sen2 + 1);
                    }
                } else if sen1 > sen2 {
                    if now >= sen1 || sen1 - sen2 == 1 {
                        tf = false;
                        break;
                    }
                    now = max(now, sen2 + 1);
                }
            }
        }
    }
    
    if tf {
        writeln!(output,"YES").unwrap();
    } else {
        writeln!(output,"NO").unwrap();
    };
    print!("{}",output);
}

// 제출 번호 : 86066309, 메모리 : 13212, 시간 : 28