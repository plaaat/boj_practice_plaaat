use std::
    io::{self, BufRead}
;

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let x = input();
    let res = match x.as_str() {
        "M" => "MatKor",
        "W" => "WiCys",
        "C" => "CyKor",
        "A" => "AlKor",
        _ => "$clear"
    };
    print!("{}",res)
}

// 제출번호 : 87576359, 메모리 : 13204, 시간 : 0