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
    let inp1 = input();
    let inp2 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let mut inp2 = inp2.split_ascii_whitespace();
    let (h,w):(i32,i32) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );
    let (mut c,mut d):(i32,i32) = (
        inp2.next().unwrap().parse().unwrap(),
        inp2.next().unwrap().parse().unwrap()
    );

    let mut ans = vec![vec![0; w as usize]; h as usize];
    let mut prev = 0;

    for i in 0..h as usize {
        let min_sum: i32 = if i == 0 { 0 } else { prev + 1 };
        let mut now = 0;
        let mut j = 0;

        let nines = (if min_sum > c.min(w) {min_sum-((c.min(w))) + 8} else {0}) / 9;
        
        if nines > d || c + d < w {
            println!("-1");
            return;
        }

        while j < w as usize && j < nines as usize {
            ans[i][j] = 9;
            now += 9;
            d -= 1;
            j += 1;
        }

        while j < w as usize && c > 0 {
            ans[i][j] = 1;
            now += 1;
            c -= 1;
            j += 1;
        }

        while j < w as usize && d > 0 {
            ans[i][j] = 9;
            now += 9;
            d -= 1;
            j += 1;
        }

        if now <= prev && i > 0 {
            println!("-1");
            return;
        }

        prev = now;
    }

    if c > 0 || d > 0 {
        writeln!(res, "-1").unwrap();
    } else {
        for i in 0..h as usize {
            for j in 0..w as usize {
                write!(res, "{}", ans[i][j]).unwrap();
                if j < w as usize - 1 {
                    write!(res, " ").unwrap();
                }
            }
            writeln!(res).unwrap();
        }
    }
    print!("{}", res);
}