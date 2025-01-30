use std::{fmt::Write,io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let t:i32 = input().parse().unwrap();
    let mut t1 = (0,0);
    let mut t2 = (0,0);
    let mut last = (0,0);
    let mut win1 = 0;

    for i in 0..t {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let team:i32 = inp2.next().unwrap().parse().unwrap();
        let (tm,ts):(i32,i32) = inp2.next().unwrap().split_once(':').map(
            |(x,y)| (x.parse().unwrap(),y.parse().unwrap())
        ).unwrap();
        
        if i == 0 {
            if team == 2 {
                win1 -= 1;
            } else {
                win1 += 1
            }
            last = (tm,ts)
        } else {
            if team == 1 {
                if win1 > 0 {
                    win1 += 1;
                    continue;
                } else if win1 == -1{
                    if last.1 > ts {
                        t2 = (t2.0 + (tm - last.0 - 1), t2.1 + (60 + ts - last.1))
                    } else {
                        t2 = (t2.0 + (tm - last.0), t2.1 + (ts - last.1))
                    }
                    last = (tm,ts);
                } else if win1 == 0 {
                    last = (tm,ts);
                }
                win1 += 1
            } else {
                if win1 < 0 {
                    win1 -= 1;
                    continue;
                } else if win1 == 1 {
                    if last.1 > ts {
                        t1 = (t1.0 + tm - last.0 - 1, t1.1 + ts + 60 - last.1)
                    } else {
                        t1 = (t1.0 + tm - last.0, t1.1 + ts - last.1)
                    }
                    last = (tm,ts);
                } else if win1 == 0 {
                    last = (tm,ts)
                }
                win1 -= 1;
            }
        }
    }

    if win1 > 0 {
        t1 = (t1.0 + (47 - last.0), t1.1 + (60 - last.1))
    } else if win1 < 0{
        t2 = (t2.0 + (47 - last.0), t2.1 + (60 - last.1))
    }

    t1 = (t1.0 + t1.1 / 60, t1.1 % 60);
    t2 = (t2.0 + t2.1 / 60, t2.1 % 60);

    writeln!(res,"{:0>2}:{:0>2}",t1.0,t1.1).unwrap();
    writeln!(res,"{:0>2}:{:0>2}",t2.0,t2.1).unwrap();
    print!("{res}")
}

// 제출 번호 : 89338825, 메모리 : 13208, 시간 : 0