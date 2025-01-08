use std::{
    fmt::Write,
    io::{self, BufRead},
    collections::HashMap
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();
    let inp1 = input();
    let inp1:Vec<&str> = inp1.split_ascii_whitespace().collect();
    let mut dic = HashMap::with_capacity(n as usize);
    for i in 0..inp1.len() {
        let wo = inp1[i];
        if dic.contains_key(wo) {
            *dic.get_mut(wo).unwrap() += 1;
            if *dic.get(wo).unwrap() == 5 {
                writeln!(res, "{}", i + 1).unwrap();
                print!("{}", res);
                return;
            }
        } else {
            dic.insert(wo, 1);
        }
    }
    writeln!(res, "0").unwrap();
    print!("{}", res);
}