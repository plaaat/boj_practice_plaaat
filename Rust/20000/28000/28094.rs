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

fn dfs(now: i32, n: i32, visited: &mut Vec<i32>, cost: &Vec<Vec<i32>>, ans: &mut i32, ans_c: &mut i32) {
    if now == n {
        let mut sum = 0;
        for i in 1..=n as usize {
            for j in 1..=n as usize {
                if visited[i] < visited[j] {
                    sum += cost[i][j];
                }
            }
        }
        if sum > *ans {
            *ans = sum;
            *ans_c = 1;
        } else if sum == *ans {
            *ans_c += 1;
        }
        return;
    }

    for i in 1..visited.len() {
        if visited[i] == -1 {
            visited[i] = now;
            dfs(now + 1, n, visited, cost, ans, ans_c);
            visited[i] = -1;
        }
    }
}

fn main() {
    let mut res = String::new();
    let t: i32 = input().parse().unwrap();
    
    for _ in 0..t {
        let inp1 = input();
        let mut inp1 = inp1.split_whitespace();
        let n: i32 = inp1.next().unwrap().parse().unwrap();
        let m: i32 = inp1.next().unwrap().parse().unwrap();
        
        let mut cost = vec![vec![0; (n + 1) as usize]; (n + 1) as usize];
        
        for _ in 0..m {
            let inp2 = input();
            let mut inp2 = inp2.split_whitespace();
            let v: i32 = inp2.next().unwrap().parse().unwrap();
            let a: usize = inp2.next().unwrap().parse().unwrap();
            let b: usize = inp2.next().unwrap().parse().unwrap();
            cost[a][b] += v;
        }
        
        let mut visited = vec![-1; (n + 1) as usize];
        let mut ans = 0;
        let mut cnt = 0;
        
        dfs(0, n, &mut visited, &cost, &mut ans, &mut cnt);
        
        writeln!(res,"{} {}", ans, cnt).unwrap();
    }
    print!("{}",res)
}

// 제출 번호 : 87616389, 메모리 : 13212, 시간 : 0
