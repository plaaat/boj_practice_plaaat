use std::
    io::{self, stdout, BufRead, Write};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut ans_v = vec![2;100];
    let mut win:i32 = input().parse().unwrap();
    for i in 0..100 {
        if win == 100 {break;}
        ans_v[i] = 0;
        println!("? {}",ans_v.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(""));
        stdout().flush().unwrap();
        
        let tn:i32 = input().parse().unwrap();
        if tn < win {
            ans_v[i] = 2
        } else if tn == win {
            ans_v[i] = 5;
            win += 1
        } else {
            win += 1
        }
    }

    let mut res = String::from("! ");
    for i in ans_v.iter() {
        let t = match *i {
            0 => '2',
            2 => '5',
            _ => '0'
        };
        res.push(t);
    }
    println!("{}",res)
}

// 제출번호 : 87578856, 메모리 : 13676, 시간 : 8
