use std::{fmt::Write,io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn perm(wo:&Vec<char>,depth:i32, k:i32, visit:&mut Vec<bool>, out:&mut Vec<char>,res: &mut String, it:&mut i32) {
    if depth != wo.len() as i32 {
        for i in 0..wo.len() {
            if visit[i] != true {
                visit[i] = true;
                out[depth as usize] = wo[i];
                perm(wo,depth+1,k,visit,out,res,it);
                visit[i] = false;
                if *it == k {
                    return;
                }
            }
        }
    } else {
        *it += 1;
        if *it != k {
            return;
        } else {
            writeln!(res,"{}",out.iter().collect::<String>()).unwrap();
            return;
        }
    }
}

fn main() {
    let mut res = String::new();
    let wo_len = Vec::from([0,1,2,6,24,120,720,5040,40320,362880,3628880]);
    loop {
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace();
        if let (Some(wo),Some(n)) = (inp1.next(),inp1.next()) {
            let n = n.parse().unwrap();
            if wo_len[wo.len()] < n {
                writeln!(res,"{wo} {n} = No permutation").unwrap();
            } else {
                let mut it = 0;
                write!(res,"{wo} {n} = ").unwrap();
                perm(
                    &wo.chars().collect::<Vec<char>>(),
                    0,
                    n,
                    &mut vec![false;wo.len()],
                    &mut vec![1 as char;wo.len()],
                    &mut res,
                    &mut it
                );
            }
        } else {
            break;
        }
    }
    print!("{res}")
}

// 제출 번호 : 89409032, 메모리 : 13212, 시간 : 136