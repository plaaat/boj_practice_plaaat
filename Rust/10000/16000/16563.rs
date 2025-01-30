use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn prime_num(n: usize) -> Vec<usize> {
    let mut primes = vec![true; n + 1];
    let mut res = Vec::new();
    for i in 2..=n {
        if primes[i] {
            res.push(i);
            let mut j = i * i;
            while j <= n {
                primes[j] = false;
                j += i;
            }
        }
    }
    res
}

fn main() {
    let mut res = String::new();
    let _: i32 = input().parse().unwrap();
    let inp1 = input();
    let nli = inp1.split_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let primes = prime_num(2250);

    for &i in &nli {
        let mut num = i as usize;
        let mut tres = String::new();
        for &p in &primes {
            if num == 1 || p > num {
                break;
            }
            while num % p == 0 {
                write!(&mut tres, "{} ", p).unwrap();
                num /= p;
            }
        }
        if num > 1 {
            write!(&mut tres, "{}", num).unwrap();
        } else {
            tres.pop();
        }
        writeln!(&mut res, "{}", tres).unwrap();
    }
    print!("{}", res);
}


#  제출 번호 : 88470284, 메모리 : 53092, 시간 : 1372