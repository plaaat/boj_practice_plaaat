use std::{
    fmt::Write,
    io::{self, BufRead}
};
fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:usize = input().parse().unwrap();
    let mut li = Vec::with_capacity(n);

    for _ in 0..n {
        let inp1 = input();
        let mut inp1 = inp1.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap());
        li.push((inp1.next().unwrap(),inp1.next().unwrap()));
    }
    
    let mut pn: i64 = 0;
    for i in 0..n {
        let (x1,y1) = li[i];
        let (x2,y2) = li[(i+1) % n];
        pn += x1 as i64 * y2 as i64 - y1 as i64 * x2 as i64
    }

    let pn = format!("{:.1}", pn.abs() as f64 / 2.0);
    writeln!(res, "{}", pn).unwrap();
    print!("{}", res)
}

// 제출 번호 : 87583805, 메모리 : 13236, 시간 : 4
