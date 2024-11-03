use std::{collections::HashMap,io};
use std::fmt::Write;

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    let inp1 = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n, m) = (
        inp1.next().unwrap().parse::<i32>().unwrap(),
        inp1.next().unwrap().parse::<i32>().unwrap()
    );

    let mut ju = HashMap::new();

    for _ in 0..m {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (c,x, h) = (
            inp2.next().unwrap().parse::<i32>().unwrap(),
            inp2.next().unwrap().parse::<i32>().unwrap(),
            inp2.next().unwrap().parse::<i32>().unwrap()
        );
        ju.insert(x, (h,c));
    }
    
    let mut tf = true;
    let mut now = 0;
    for i in 1..n {
        if ju.contains_key(&i) {
            let (juy,jud) = ju[&i];
            if jud == 0 {
                if now > juy{now -= 1}
                else{now = juy+1;}
            } else if now - juy > 0 {
                tf = false;
                break;
            } else {
                now -= 1;
            }
        }
        else {now -= 1;}
    }
    if tf && now > 1 {tf = false;};

    if tf {writeln!(output,"stay").unwrap()}
    else {writeln!(output,"adios").unwrap()}

    print!("{}", output);
}

// 제출 번호 : 85967773, 메모리 : 18224, 시간 : 68