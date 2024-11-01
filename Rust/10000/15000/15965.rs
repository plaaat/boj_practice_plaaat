use std::io::{self, BufRead};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut n: i32 = input().parse().unwrap();
    let mut nums = vec![true; 7368789];
    nums[0] = false;
    nums[1] = false;

    let lim = (7368787.0 as f64).sqrt() as usize;
    for i in 2..lim {
        if nums[i] {
            let mut ind = i * i;
            while ind <= 7368787 {
                nums[ind] = false;
                ind += i;
            }
        }
    }
    
    for (i,v ) in nums.iter().enumerate() {
        if *v {
            n -= 1;
            if n == 0 {
                println!("{i}");
                break;
            }

        }
    }
}

// 제출 번호 : 85900384, 메모리 : 20404, 시간 : 40