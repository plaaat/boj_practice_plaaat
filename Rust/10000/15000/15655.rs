use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn backtrack(nli: &Vec<i32>, n: i32, m: i32, res: &mut String, s: &mut Vec<i32>, idx: i32) {
    if s.len() == m as usize {
        writeln!(res, "{}", s.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" ")).unwrap();
        return;
    }
    for i in idx..n {
        s.push(nli[i as usize]);
        backtrack(nli, n, m, res, s, i + 1);
        s.pop();
    }
}
fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1:Vec<i32> = inp1.split_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n,m) = (inp1[0], inp1[1]);
    let inp2 = input();
    let mut nli:Vec<i32> = inp2.split_whitespace().map(|x| x.parse().unwrap()).collect();
    nli.sort_unstable();
    let s = &mut Vec::new();
    backtrack(&nli, n, m, &mut res, s, 0);
    print!("{}", res);
}

// 제출번호 : 88827463, 메모리 : 13220, 시간 : 0 