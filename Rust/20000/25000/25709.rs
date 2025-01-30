use std::{
    fmt::Write,
    collections::{VecDeque, HashSet},
    io::{self, BufRead}
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn find1(mut num: i32) -> i32 {
    let mut ind = 1;
    let mut res = 0;
    let mut tf = false;

    while num > 0 {
        let step = num % 10;
        if step == 1 && !tf {
            tf = true;
        } else {
            res += step * ind;
            ind *= 10;
        }
        num /= 10;
    }
    res
}

fn main() {
    let mut res = String::new();
    let n: i32 = input().parse().unwrap();
    let mut pn = 1_000_000_000;
    let mut vis = HashSet::new();
    let mut q = VecDeque::new();
    q.push_back((n, 0));

    while !q.is_empty() {
        let (now, count) = q.pop_front().unwrap();

        if now == 0 {
            pn = pn.min(count);
            continue;
        }
        if count + 1 > pn || vis.contains(&now) {
            continue;
        }
        vis.insert(now);

        q.push_back((now - 1, count + 1));

        if now >= 10 && now.to_string().contains('1') {
            q.push_back((find1(now), count + 1));
        }
    }

    writeln!(res, "{}", pn).unwrap();
    print!("{}", res);
}



#  제출 번호 : 86799747, 메모리 : 13216, 시간 : 0