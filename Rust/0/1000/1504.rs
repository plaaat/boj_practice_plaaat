use std::{
    fmt::Write,
    io::{self, BufRead},
    collections::HashMap,
    collections::BinaryHeap,
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace()
        .map(|x| x.parse::<i32>().unwrap());
    let (n, e) = (inp1.next().unwrap(), inp1.next().unwrap());

    let mut graph: Vec<Vec<(i32, i32)>> = vec![Vec::new(); (n + 1) as usize];
    for _ in 0..e {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace()
            .map(|x| x.parse().unwrap());

        let (a, b, c) = (inp2.next().unwrap(), inp2.next().unwrap(), inp2.next().unwrap());
        graph[a as usize].push((b, c));
        graph[b as usize].push((a, c));
    }
    
    let inp3 = input();
    let mut inp3 = inp3.split_ascii_whitespace()
        .map(|x| x.parse().unwrap());
    let (v1, v2) = (inp3.next().unwrap(), inp3.next().unwrap());

    let mut min_cost = i32::MAX;
    let mut vis = HashMap::new();
    let mut q = BinaryHeap::new();
    
    let (tf1,tf2) = match 1 {
        n if v1 == n => (true,false),
        n if v2 == n => (false,true),
        _ => (false,false)
    };

    q.push((0, 1, tf1, tf2));
    
    while !q.is_empty() {
        let (cost, num, fl1, fl2) = q.pop().unwrap();
        let cost = -cost;

        if num == n && fl1 && fl2 {
            min_cost = min_cost.min(cost);
            continue;
        }

        let vis_key = (num, fl1, fl2);
        if vis.get(&vis_key).map_or(false, |&last_cost| cost >= last_cost) {
            continue;
        }
        vis.insert(vis_key, cost);

        if !graph[num as usize].is_empty() {continue;}
        for &(next_n, next_co) in &graph[num as usize] {
            if cost + next_co >= min_cost {
                continue;
            }
            
            let (tfl1, tfl2) = match next_n {
                n if n == v1 => (true, fl2),
                n if n == v2 => (fl1, true),
                _ => (fl1, fl2)
            };

            q.push((-(cost + next_co), next_n, tfl1, tfl2));
        }
    }

    if min_cost < i32::MAX { 
        writeln!(res,"{}",min_cost).unwrap() 
    } else { 
        writeln!(res,"-1").unwrap()
    };
    print!("{}", res);
}

// 제출번호 : 87278441, 메모리 : 29064, 시간 : 328