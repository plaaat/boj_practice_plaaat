use std::{
    fmt::Write,
    io::{self, BufRead},
    collections::BinaryHeap,
    cmp::Reverse,
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

struct Finder {
    dist: Vec<i32>,
    q: BinaryHeap<Reverse<(i32, usize)>>,
}

impl Finder {
    fn new(n: usize, a: usize) -> Self {
        let mut dist = vec![100_000_007; n + 1];
        dist[a] = 0;
        let mut q = BinaryHeap::new();
        q.push(Reverse((0, a)));
        Finder { dist, q }
    }

    fn dijk(&mut self, graph: &Vec<Vec<(usize, i32)>>) -> Vec<i32> {
        while let Some(Reverse((nowd, now))) = self.q.pop() {
            if self.dist[now] < nowd {
                continue;
            }

            for &(t, co) in &graph[now] {
                let new_dist = nowd + co;
                if new_dist < self.dist[t] {
                    self.dist[t] = new_dist;
                    self.q.push(Reverse((new_dist, t)));
                }
            }
        }
        self.dist.clone()
    }
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n, m, x) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
    );

    let mut graph = vec![vec![]; n as usize + 1];
    let mut graph_rev = vec![vec![]; n as usize + 1];
    
    for _ in 0..m {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (a, b, c): (usize, usize, i32) = (
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap(),
        );
        graph[a].push((b, c));
        graph_rev[b].push((a, c));
    }

    let mut findx = Finder::new(n, x);
    let mut prli = findx.dijk(&graph);
    prli[0] = 0;

    let mut findx_rev = Finder::new(n, x);
    let dist_rev = findx_rev.dijk(&graph_rev);

    for i in 1..n + 1 {
        if i == x { continue; }
        prli[i] += dist_rev[i];
    }

    prli.sort_unstable();
    writeln!(res, "{}", prli[n]).unwrap();
    print!("{}", res);
}

// 제출 번호 : 87193838, 메모리 : 13616, 시간 : 4
