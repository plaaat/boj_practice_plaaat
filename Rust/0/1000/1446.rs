use std::{collections::HashMap, fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    
    let (n,d):(i32,usize) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );
    
    let mut vis = vec![d as i32;d+1];
    let mut dis: HashMap<usize, Vec<(i32, i32)>> = HashMap::with_capacity(n as usize);
    
    for _ in 0..n {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (a,b,c):(usize,i32,i32) = (
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap()
        );
        if b > (d as i32){continue;}

        if dis.contains_key(&a) {
            dis.get_mut(&a).unwrap().push((b,c));
        } else {
            dis.insert(a, vec![(b,c)]);
        }
    }
    vis[0] = 0;
    vis[1] = 1;
    for i in 0..d {
        vis[i+1] = vis[i+1].min(vis[i] + 1);
        if dis.contains_key(&i) {
            let lis = dis.get(&i).unwrap();
            for (a,b) in lis.iter() {
                vis[*a as usize] = vis[*a as usize].min(b + vis[i])
            }
        }
    }
    writeln!(res,"{}",vis[d]).unwrap();
    print!("{}", res);
}

// 제출 번호 : 86550280, 메모리 : 13216, 시간 : 0
