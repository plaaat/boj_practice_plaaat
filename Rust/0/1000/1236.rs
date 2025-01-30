use std::{fmt::Write,io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1 = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect::<Vec<i32>>();
    let (n,m) = (inp1[0],inp1[1]);
    let mut ga = vec![false; m as usize];
    let mut se = vec![false; n as usize];

    for i in 0..n {
        let inp2 = input();
        let inp2 = inp2.as_bytes();
        for j in 0..m {
            if inp2[j as usize] == 'X' as u8 {
                ga[j as usize] = true;
                se[i as usize] = true 
            }
        }
    }
    
    let (mut gan, mut sen) = (0,0);
    for i in ga {
        if !i {gan += 1}
    }
    for i in se {
        if !i {sen += 1}
    }

    writeln!(res,"{}",gan.max(sen)).unwrap();
    print!("{res}")
}

// 제출 번호 : 89333056, 메모리 : 13208, 시간 : 0