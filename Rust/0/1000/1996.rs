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
    let n:i32 = input().parse().unwrap();
    let mut map = Vec::with_capacity(n as usize);

    for _ in 0..n {
        let wo = input();
        let wo_li: Vec<char> = wo.chars().collect();
        map.push(wo_li)
    }
    let di = vec![
        (1,1),(1,0),(1,-1),
        (0,1),(0,-1),
        (-1,1),(-1,0),(-1,-1)
        ];
    for i in 0..n{
        for j in 0..n {
            let mut tn = 0;
            if !(map[i as usize][j as usize] == '.') {
                write!(res,"*").unwrap();
                continue;
            }
            for (mut x,mut y) in di.iter() {
                x += j;
                y += i;
                if x >= 0 && x < n && y >= 0 && y < n {
                    if !(map[y as usize][x as usize] == '.') {
                        tn += map[y as usize][x as usize] as i32 - 48
                    }
                }
                if tn >= 10 {break;}
            }
            if tn >= 10 {write!(res,"M").unwrap()}
            else {write!(res,"{}",tn).unwrap()}
        }
        writeln!(res,"").unwrap()
    }
    print!("{}", res);
}

// 제출 번호 : 87247947, 메모리 : 18200, 시간 : 60
