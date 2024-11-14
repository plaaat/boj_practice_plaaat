use std::io::{self, BufRead};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn min(a: i32, b: i32) -> i32 {
    if a < b { return a }
    b 
}

fn dfs(t: i32, now: i32, li: &[i32], a: &[(i32, i32)], n: usize, mn: &mut i32) {
    if t >= *mn {
        return;
    }

    if now <= 0 {
        *mn = min(*mn, t);
        return;
    }

    let mut tf = false;
    for i in 0..n {
        if li[i] + a[i].0 <= t {
            tf = true;
            let mut tmp = li.to_owned();
            tmp[i] = t;
            dfs(t + 1, now - a[i].1, &tmp, a, n, mn);
        }
    }

    if !tf {
        dfs(t + 1, now, li, a, n, mn);
    }
}

fn main() {
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n, h): (usize, i32) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );

    let mut a = Vec::with_capacity(n);
    for _ in 0..n {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (c, d): (i32, i32) = (
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap()
        );
        a.push((c, d));
    }

    let tli = vec![-10000; n];
    let mut mn = 10000;
    dfs(0, h, &tli, &a, n, &mut mn);
    println!("{}", mn);
}

// 제출 번호 : 86298664, 메모리 : 18208, 시간 : 28