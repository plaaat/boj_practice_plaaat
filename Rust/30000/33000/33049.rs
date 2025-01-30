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
    let nums: Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (mut p,mut pp,mut ppp) = (nums[0], nums[1],nums[2]);
    let mut p3 = p/3;
    let mut p4 = pp / 4;
    p %= 3;
    pp %= 4;

    if pp != 0 {
        if 4 - pp <= ppp {
            p4 += 1;
            ppp -= 4 - pp;
        } else {
            println!("-1");
            return;
        }
    }

    if p != 0 {
        if 3 - p <= ppp {
            p3 += 1;
            ppp -= 3 - p;
        } else {
            println!("-1");
            return;
        }
    }

    let mut found = false;
    for i in 0..=ppp/3 {
        let remain = ppp - (i * 3);
        if remain % 4 == 0 {
            p3 += i;
            p4 += remain / 4;
            found = true;
            break;
        }
    }

    if !found {
        println!("-1");
        return;
    }

    writeln!(res, "{} {}", p3, p4).unwrap();
    print!("{}", res);
}



#  제출 번호 : 87903886, 메모리 : 13208, 시간 : 0