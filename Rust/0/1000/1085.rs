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
    let inp1:Vec<i32> = inp1.split_ascii_whitespace()
                .map(|x| x.parse().unwrap()).collect();
    let (x,y,w,h) = (inp1[0],inp1[1],inp1[2],inp1[3]);
    let mut min = i32::MAX;
    min = min.min(w-x);
    min = min.min(x);
    min = min.min(h-y);
    min = min.min(y);
    writeln!(res,"{}",min).unwrap();
    print!("{}", res);
}



#  제출 번호 : 87716959, 메모리 : 13208, 시간 : 0