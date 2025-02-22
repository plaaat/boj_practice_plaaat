use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn tri(n:i32) -> Vec<String> {
    if n == 3 {
        vec!["  *  ".to_string()," * * ".to_string(),"*****".to_string()]
    } else {
        let last = tri(n/2);
        let mut out = vec![];
        let step = " ".repeat((n/2) as usize);
        
        for wo in &last {
            out.push(format!("{step}{wo}{step}"));
        }
        for wo in last {
            out.push(format!("{wo} {wo}"));
        }
    
        out
    }
}

fn main() {
    let mut res = String::new();
    let t = input().parse().unwrap();
    let out = tri(t);
    for wo in out {
        writeln!(res,"{wo}").unwrap()
    }
    print!("{res}")
}

// 제출 번호 : 90077015, 메모리 : 70344, 시간 : 52