use std::{
    io::{self, BufRead,},
    collections::{VecDeque, HashSet}
};
fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn bfs(x: i32, tree:Vec<Vec<(i32,i32)>>) -> (i32,i32) {
    let mut q = VecDeque::new();
    q.push_back((x,0));
    let mut vis = HashSet::new();
    vis.insert(x);
    let mut res = (0,0);
    while let Some((node, cost)) = q.pop_front() {
        for (tn,tc) in tree[node as usize].iter() {
            if !vis.contains(tn) {
                q.push_back((*tn, tc + cost));
                vis.insert(*tn);
                if res.1 < cost + tc {
                    res = (*tn,cost+tc)
                }
            }
        } 
    } 
    res
}

fn main() {
    let t:i32 = input().parse().unwrap();
    let mut tree = vec![vec![];t as usize + 1];
    
    for _ in 0..t {
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap());
        let now = inp1.next().unwrap();
        while let (Some(node),Some(cost)) = (inp1.next(),inp1.next()) {
            tree[now as usize].push((node,cost));
        }
    }
    let start = bfs(1,tree.clone()).0;
    println!("{}",bfs(start,tree).1)
}

// 제출번호 : 87581294, 메모리 : 30052, 시간 : 84
