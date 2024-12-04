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
    let mut inp1 = inp1.split_whitespace();
    let (n, m) = {
        (
            inp1.next().unwrap().parse::<i32>().unwrap(),
            inp1.next().unwrap().parse::<i32>().unwrap(),
        )
    };
    
    let probli = (1..=n).collect::<Vec<i32>>();
    
    let mut stu = vec![Vec::new(); m as usize];
    for i in 0..m {
        let inp = input();
        let mut iter = inp.split_whitespace();
        let x = iter.next().unwrap().parse::<i32>().unwrap();
        for _ in 0..x {
            let p: i32 = iter.next().unwrap().parse().unwrap();
            stu[i as usize].push(p);
        }
    }
    
    let mut pn = 10000;
    dfs(Vec::new(), 0, 0, m, &probli, &stu, &mut pn);
    
    if pn == 10000 {
        writeln!(res, "-1").unwrap();
    } else {
        writeln!(res, "{}", pn).unwrap();
    }
    print!("{}", res);
}

fn dfs(
    now: Vec<i32>,
    r: i32,
    x: i32,
    m: i32,
    probli: &Vec<i32>,
    stu: &Vec<Vec<i32>>,
    min: &mut i32
) {
    if x == m {
        if probli.iter().all(|p| now.contains(p)) && r < *min {
            *min = r;
        }
        return;
    }
    
    dfs(now.clone(), r, x + 1, m, probli, stu, min);
    
    let mut tnow = now.clone();
    tnow.extend(&stu[x as usize]);
    dfs(tnow, r + 1, x + 1, m, probli, stu, min);
}

// 제출 번호 : 87081986, 메모리 : 13212, 시간 : 0ms
