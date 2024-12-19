use std::{
    io::{self, BufRead},
    collections::{VecDeque, HashSet, HashMap},
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn bfs(x: i32, tree: &HashMap<i32, Vec<(i32, i32)>>) -> (i32, i32) {
    let mut q = VecDeque::new();
    q.push_back((x, 0));
    let mut vis = HashSet::new();
    vis.insert(x);
    let mut res = (0, 0);
    
    while let Some((node, cost)) = q.pop_front() {
        if let Some(branch) = tree.get(&node) {
            for (tn, tc) in branch {
                if !vis.contains(tn) {
                    q.push_back((*tn, cost + tc));
                    vis.insert(*tn);
                    if res.1 < cost + tc {
                        res = (*tn, cost + tc);
                    }
                }
            }
        }
    }
    res
}

fn main() {
    let t: i32 = input().parse().unwrap();
    let mut tree: HashMap<i32, Vec<(i32, i32)>> = HashMap::new();
    
    for _ in 0..(t - 1) {
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap());
        let (a, b, c) = (inp1.next().unwrap(), inp1.next().unwrap(), inp1.next().unwrap());
        
        tree.entry(a).or_default().push((b, c));
        tree.entry(b).or_default().push((a, c));
    }
    
    let start = bfs(1, &tree).0;
    println!("{}", bfs(start, &tree).1);
}

// 제출 번호 : 87542011, 메모리 : 14476, 시간 : 8
