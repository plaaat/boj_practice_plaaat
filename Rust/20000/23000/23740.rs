use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let mut res = String::new();
    let t: i32 = input().parse().unwrap();
    let mut bus: Vec<(i32, i32, i32)> = Vec::with_capacity(t as usize);
    
    for _ in 0..t {
        let inp1 = input();
        let inp1 = inp1.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
        let (a, b, c) = (inp1[0], inp1[1], inp1[2]);
        bus.push((a, b, c));
    }

    bus.sort_unstable_by_key(|x| x.0);

    let mut route: Vec<(i32, i32, i32)> = vec![];
    let mut now = bus[0];

    for &(a, b, c) in &bus[1..] {
        if now.1 >= a {
            now = (now.0, now.1.max(b), now.2.min(c));
        } else {
            route.push(now);
            now = (a, b, c);
        }
    }
    route.push(now);

    writeln!(res, "{}", route.len()).unwrap();
    for (a, b, c) in route {
        writeln!(res, "{} {} {}", a, b, c).unwrap();
    }
    print!("{}", res);
}



#  제출 번호 : 88020612, 메모리 : 26832, 시간 : 96