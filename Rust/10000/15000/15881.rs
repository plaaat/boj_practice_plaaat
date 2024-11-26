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
    let n: usize = input().parse().unwrap();
    let inp1 = input();
    if n <= 3 {
        writeln!(res, "{}", 0).unwrap();
    } else {
        let pat = inp1.split("pPAp").count() - 1;
        writeln!(res, "{}", pat).unwrap();
    }
    print!("{}", res);
}

// 제출 번호 : 86690747, 메모리 : 15220, 시간 : 4 
