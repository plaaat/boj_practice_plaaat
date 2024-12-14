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

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n, m, k, t, p): (i64, i64, i64, i64, i64) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap(),
    );
    
    let mut mo: Vec<((i64, i64), i64)> = Vec::with_capacity((k + 1) as usize);
    mo.push(((0, 0), 0)); // 더미 요소 추가

    for _ in 1..=k {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (r, c, s): (i64, i64, i64) = (
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap(),
            inp2.next().unwrap().parse().unwrap(),
        );
        
        mo.push(((r, c), s));
    }

    mo[1..].sort_by(|x, y| x.0.cmp(&y.0));

    let mut woo_c = 0;
    let mut ar_c = 0;

    {
        let mut tmo = mo.clone();
        loop {
            let mut hp = 0;
            let mut tmpc = 1;

            for i in 1..k {
                hp += (tmo[i as usize + 1].0.0 - tmo[i as usize].0.0).abs() + 
                       (tmo[i as usize + 1].0.1 - tmo[i as usize].0.1).abs();

                if hp > t {
                    break;
                }

                tmpc += 1;
            }

            woo_c = woo_c.max(tmpc);

            let mut i = k;
            while i > 1 && tmo[i as usize - 1].0 >= tmo[i as usize].0 {
                i -= 1;
            }

            if i == 1 {
                break;
            }

            let mut j = k;
            while tmo[j as usize].0 <= tmo[i as usize - 1].0 {
                j -= 1;
            }

            tmo.swap(i as usize - 1, j as usize);
            tmo[i as usize..].reverse();
        }
    }

    for i in 1..=n {
        for j in 1..=m {
            let mut tmpc = 0;

            for k in 1..=k {
                let dist = (mo[k as usize].0.0 - i).abs() + (mo[k as usize].0.1 - j).abs();
                
                if p >= mo[k as usize].1 * dist {
                    tmpc += 1;
                }
            }

            ar_c = ar_c.max(tmpc);
        }
    }

    writeln!(res, "{} {}", woo_c, ar_c).unwrap();
    print!("{}", res);
}

// 제출 번호 : 87454055, 메모리 : 13216, 시간 : 80