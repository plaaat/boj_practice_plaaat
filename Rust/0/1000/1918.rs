use std::{
    collections::HashMap,
    fmt::Write,
    io::{self, BufRead},
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let wo = input();
    let mut dic = HashMap::with_capacity(4);
    dic.insert('+', 1);
    dic.insert('-', 1);
    dic.insert('*', 2);
    dic.insert('/', 2);
    let mut stack = vec![];
    let mut prsta = vec![];
    
    for i in wo.chars() {
        if i.is_alphabetic() {
            prsta.push(i);
        } else if i == '(' {
            stack.push(i);
        } else if i == ')' {
            while let Some(wo) = stack.pop() {
                if wo == '(' {
                    break;
                }
                prsta.push(wo);
            }
        } else {
            while let Some(&wo) = stack.last() {
                if wo == '(' {
                    break;
                } else if dic.get(&wo).unwrap_or(&0) < dic.get(&i).unwrap_or(&0) {
                    break;
                }
                prsta.push(stack.pop().unwrap());
            }
            stack.push(i);
        }
    }
    
    while let Some(wo) = stack.pop() {
        prsta.push(wo);
    }

    writeln!(res, "{}", prsta.iter().collect::<String>()).unwrap();
    print!("{}", res);
}

// 제출번호 : 87336011, 메모리 : 13216, 시간 : 0