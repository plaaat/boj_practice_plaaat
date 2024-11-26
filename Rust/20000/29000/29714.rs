use std::{
    fmt::Write,
    io::{self, BufRead},
    collections::HashMap,
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n = input().parse::<i32>().unwrap();
    let nli = input()
        .split_whitespace()
        .map(|s| s.parse::<i32>().unwrap())
        .collect::<Vec<i32>>();
    let t = input().parse::<i32>().unwrap();
    
    let mut guli: HashMap<i32, i32> = HashMap::with_capacity(n as usize);
    for i in nli.iter() {
        *guli.entry(*i).or_insert(0) += 1;
    }

    for _ in 0..t {
        let mut tguli: HashMap<i32, i32> = HashMap::new();
        let a = input()
            .split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        let b = input()
            .split_whitespace()
            .map(|s| s.parse::<i32>().unwrap())
            .collect::<Vec<i32>>();
        let an = a[0] as usize;
        let bn = b[0] as usize;
        let mut flag = true;
        
        if an > 0 {
            for i in 1..=an {
                if guli.contains_key(&a[i]) {
                    *tguli.entry(a[i]).or_insert(0) += 1;
                } else {
                    flag = false;
                    break;
                }
            }
        }
        if !flag {
            continue;
        }

        for (&key, &val) in tguli.iter() {
            if guli.get(&key).unwrap_or(&0) < &val {
                flag = false;
                break;
            }
        }
        if !flag {continue;}
        
        for (&key, &val) in tguli.iter() {
            if let Some(count) = guli.get_mut(&key) {
                *count -= val;
                if *count == 0 {
                    guli.remove(&key);
                }
            }
        }
        
        if bn > 0 {
            for i in 1..=bn {
                *guli.entry(b[i]).or_insert(0) += 1;
            }
        }
    }
    
    let pn: i32 = guli.values().sum();
    writeln!(res, "{}", pn).unwrap();
    if pn != 0 {
        let keys: Vec<_> = guli.keys().collect();
        let mut prgu = vec![];
        for &key in keys {
            for _ in 0..guli[&key] {
                prgu.push(key);
            }
        }
        let gures = prgu.iter()
            .map(|x| x.to_string())
            .collect::<Vec<String>>()
            .join(" ");
        writeln!(res, "{}", gures).unwrap();
    }
    print!("{}", res);
}

// 제출 번호 : 86891629, 메모리 : 43192, 시간 : 168 