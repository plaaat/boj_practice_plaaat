use std::{fmt::Write, io};

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut output = String::new();
    
    let inp1 = input();
    let mut inp1 = inp1.split(":");
    let (mut hh,mut mm) : (i32,i32) = (
        inp1.next().unwrap().parse().unwrap(),
        inp1.next().unwrap().parse().unwrap()
    );

    let inp2 = input();
    let mut patli:Vec<i32> = inp2
        .split_ascii_whitespace()
        .map(|x| x.parse().unwrap())
        .collect();
    let mut pn = 0;
    let t:i32 = input().parse().unwrap();
    
    for _ in 0..t {
        let inp3 = input();
        let mut inp3 = inp3.split_ascii_whitespace();
        let nom:f64 = inp3.next().unwrap().parse().unwrap();
        if nom >= 60.0 {
            break;
        }

        let wo:&str = inp3.next().unwrap();
        
        if mm >= 60 {mm-=60;hh+=1} 
        if hh > 11 {hh-=12};
        
        match wo{
            "10MIN" => mm += 10,
            "30MIN" => mm += 30,
            "50MIN" => mm += 50,
            "2HOUR" => hh += 2,
            "4HOUR" => hh += 4,
            "9HOUR" => hh += 9,
            _=>patli[(hh/2) as usize] = 0,
        }
        
    }

    for i in patli.iter() {
        pn += i
    };

    if pn > 100 {
        writeln!(output,"100").unwrap()
    } else {
        writeln!(output,"{}",pn).unwrap()
    }

    print!("{}",output);
}

// 제출 번호 : 86197949, 메모리 : 13232, 시간 : 0