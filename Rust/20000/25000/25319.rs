use std::{fmt::Write,io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1:Vec<usize> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n,m) = (inp1[0],inp1[1]);
    let mut v: Vec<Vec<(usize, usize)>> = vec![vec![]; 26];

    for i in 0..n {
        let inp2 = input();
        for (j, ch) in inp2.chars().enumerate() {
            v[ch as usize - 'a' as usize].push((i, j));
        }
    }

    let s = input();
    let mut wos = vec![0; 26];
    for ch in s.chars() {
        wos[ch as usize - 'a' as usize] += 1;
    }

    let mut ans_c = usize::MAX;

    for ch in s.chars() {
        let idx = ch as usize - 'a' as usize;
        ans_c = ans_c.min(v[idx].len() / wos[idx]);
    }

    let mut l = String::new();

    let drul = |cur: &mut (usize, usize), target: (usize, usize), l: &mut String| {
        let dr = target.0 as isize - cur.0 as isize;
        let dc = target.1 as isize - cur.1 as isize;

        let rc = if dr > 0 { 'D' } else { 'U' };
        let cc = if dc > 0 { 'R' } else { 'L' };

        for _ in 0..dr.abs() {
            l.push(rc);
        }
        for _ in 0..dc.abs() {
            l.push(cc);
        }
    };

    let mut cur = (0, 0);

    for _ in 0..ans_c {
        for ch in s.chars() {
            let idx = ch as usize - 'a' as usize;
            let target = v[idx].pop().unwrap();
            drul(&mut cur, target, &mut l);
            l.push('P');
            cur = target;
        }
    }

    let tmp = (n - 1, m - 1);
    drul(&mut cur, tmp, &mut l);

    writeln!(res,"{} {}", ans_c, l.len()).unwrap();
    writeln!(res,"{}", l).unwrap();
    print!("{res}")
}

// 제출 번호 : 89264898, 메모리 : 13524, 시간 : 0