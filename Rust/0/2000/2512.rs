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
    let _: i32 = input().parse().unwrap();
    let inp1 = input();
    let nli: Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let m: i32 = input().parse().unwrap();

    let mut low = 0;
    let mut high: i32 = nli.iter().sum();
    let mut maxlim = 0;
    let &highn = nli.iter().max().unwrap();
    
    while low <= high {
        let mid = (low + high) / 2;
        let sumnum: i32 = nli
            .iter()
            .map(|x| if *x > mid { mid } else { *x })
            .sum();

        if sumnum <= m {
            maxlim = mid;
            low = mid + 1;
        } else {
            high = mid - 1;
        }
    }
    writeln!(res,"{}",maxlim.min(highn)).unwrap();
    print!("{}", res);
}

// 제출 번호 : 87888374, 메모리 : 13396, 시간 : 0
