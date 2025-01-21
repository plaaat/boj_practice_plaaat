use std::{io::{self, BufRead}, collections::HashMap};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}
fn main() {
    let mut res = String::new();
    let hh = input().parse::<i32>().unwrap();
    let mm = input().parse::<i32>().unwrap();
    let mut h = HashMap::new();
    let words = vec![
        "one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten",
        "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen", "seventeen",
        "eighteen", "nineteen", "twenty", "twenty one", "twenty two", "twenty three",
        "twenty four", "twenty five", "twenty six", "twenty seven", "twenty eight",
        "twenty nine", "thirty",
    ];

    for (i, word) in words.iter().enumerate() {
        h.insert(i as i32 + 1, *word);
    }
    if mm == 0 {
        res.push_str(&format!("{} o' clock", h.get(&hh).unwrap()));
    } else if mm == 1 {
        res.push_str(&format!("one minute past {}", h.get(&hh).unwrap()));
    } else if mm == 59 {
        res.push_str(&format!("one minute to {}", if hh != 12 {h.get(&(hh + 1)).unwrap()} else {h.get(&1).unwrap()}));
    } else if mm == 15 {
        res.push_str(&format!("quarter past {}", h.get(&hh).unwrap()));
    } else if mm == 30 {
        res.push_str(&format!("half past {}", h.get(&hh).unwrap()));
    } else if mm == 45 {
        res.push_str(&format!("quarter to {}", if hh != 12 {h.get(&(hh + 1)).unwrap()} else {h.get(&1).unwrap()}));
    } else if mm == 60 {
        res.push_str(&format!("{} o' clock", if hh != 12 {h.get(&(hh + 1)).unwrap()} else {h.get(&1).unwrap()}));
    } else if mm < 30 {
        res.push_str(&format!("{} minutes past {}", h.get(&mm).unwrap(), h.get(&hh).unwrap()));
    } else {
        res.push_str(&format!(
            "{} minutes to {}",
            h.get(&(60 - mm)).unwrap(),
            if hh != 12 {h.get(&(hh + 1)).unwrap()} else {h.get(&1).unwrap()}
        ));
    }

    println!("{}", res);
}

// 제출번호 : 88824989, 메모리 : 13224, 시간 : 0 