use std::{collections::HashMap,io};
use std::fmt::Write;

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}
struct Finder {
    dp: HashMap<i32,i32>,
}

impl Finder {
    fn new() -> Self {
        let mut dp = HashMap::new();
        dp.insert(1, 1);
        dp.insert(2, 2);
        dp.insert(3, 3);
        Finder { dp }
    }

    fn cal(&mut self, n:i32) -> i32 {
        if let Some(&val) = self.dp.get(&n) {
            return val;

        } else{
            let mut val = self.cal(n - 1) + self.cal(n - 2) - self.cal(n - 3);
            if n % 3 == 0 {val += 1};
            self.dp.insert(n, val);
            val
        } 
    }
}

fn main() {
    let mut output = String::new();
    let t: i32 = input().parse().unwrap();
    let mut find = Finder::new();

    for _ in 0..t {
        let n :i32 = input().parse().unwrap();
        let n = find.cal(n);
        writeln!(output,"{}",n).unwrap();
    }

    print!("{}", output);
}

// 제출 번호 : 85983650, 메모리 : 13848, 시간 : 4