use std::{
    collections::{HashMap,VecDeque}, fmt::Write, io::{self, BufRead}
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let n:i32 = input().parse().unwrap();
    let inp1 = input();
    let inp1:Vec<&str> = inp1.split_ascii_whitespace().collect();
    let mut dic: HashMap<&str, VecDeque<usize>> = HashMap::with_capacity(n as usize);
    let mut minx = i32::MAX;
    for i in 0..inp1.len() {
        let wo = inp1[i];
        if dic.contains_key(wo) {
            dic.get_mut(wo).unwrap().push_back(i);
            if dic.get(wo).unwrap().len() == 5 {
                minx = minx.min((i - dic.get(wo).unwrap()[0] + 1) as i32);
                dic.get_mut(wo).unwrap().pop_front();
            }
        } else {
            dic.insert(wo, VecDeque::from([i]));
        }
    }

    if minx == i32::MAX {
        minx = -1;
    }

    writeln!(res, "{}",minx).unwrap();
    print!("{}", res);
}


#  제출 번호 : 87898682, 메모리 : 22236, 시간 : 16