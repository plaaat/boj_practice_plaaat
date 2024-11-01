use std::{collections::HashMap, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let inp = input();
    let inp:Vec<&str> = inp
    .trim().split_ascii_whitespace().collect();
    
    let n: i32 = inp[0].parse().unwrap();
    let m: f64 = inp[1].parse().unwrap();

    let mut tot:f64 = 0.0;
    let mut num:f64 = 0.0;
    let score= HashMap::from([
        ("F", 0.00), ("D0", 1.00), ("D+", 1.50), ("C0", 2.00),
        ("C+", 2.50), ("B0", 3.00), ("B+", 3.50), ("A0", 4.00), 
        ("A+", 4.50)]);
    
    for _ in 1..n {
        let inp = input();
        let mut inp = inp.split_ascii_whitespace();
        
        if let (Some(n),Some(wo)) = (inp.next(),inp.next()) {
            let n: f64 = n.parse().unwrap();
            let val = score.get(wo).unwrap();
            tot += n * val;
            num += n;
        }
    }

    let x: f64 = input().parse().unwrap();
    let minnum: f64 = 1e-10;
    let mut tf = true;
    for (val,n) in score {
        if (tot + (n * x))/(num + x) > m + minnum{
            println!("{}",val);
            tf = false;
            break;
        }
    }

    if tf {
        println!("impossible");
    }
}

//모르겟다야팔..