use std::{
    fmt::Write,
    io::{self, BufRead}, vec
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn find(tox: usize, toy: usize, his: &mut Vec<Vec<bool>>, vis: &mut Vec<Vec<i64>>) -> i64 {
    for i in 1..toy {
        for j in 1..tox {
            if his[i][j] {continue;}
            vis[i][j] = vis[i][j - 1] % 1000007 + vis[i - 1][j] % 1000007;
        }
    }

    vis[toy - 1][tox - 1]
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (w,h):(usize,usize) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );
    
    let inp2 = input();
    let mut inp2 = inp2.split_ascii_whitespace();
    let (tox,toy):(usize,usize) = (
        inp2.next().unwrap().parse().unwrap(),
        inp2.next().unwrap().parse().unwrap()
    );

    let mut his = vec![vec![false;201];201];
    let mut vis = vec![vec![1;201];201];
    
    let res1 = find(tox,toy,&mut his,&mut vis);
    
    let tox = (w as i32 - tox as i32).abs() + 1;
    let toy = (h as i32 - toy as i32).abs() + 1;
    let res2 = find(tox as usize,toy as usize,&mut his,&mut vis);
    
    writeln!(res,"{}",res1*res2 % 1000007).unwrap();
    print!("{}", res);
}

// 제출 번호 : 86585615, 메모리 : 13476, 시간 : 0
