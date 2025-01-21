use std::{collections::{VecDeque, HashMap}, fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1 = inp1.split_ascii_whitespace().map(|x| x.parse::<i32>().unwrap()).collect::<Vec<i32>>();
    let (n,m) = (inp1[0], inp1[1]);
    let mut queue = VecDeque::with_capacity(n as usize);
    let mut items = vec![0;m as usize + 1];
    for _ in 0..n {
        let inp2 = input();
        let inp2:Vec<i32> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
        let (p,w) = (inp2[0],inp2[1]);
        queue.push_back((p,w));
        items[p as usize] += 1;
    }
    
    let mut low = m;
    let mut val = 0;
    let mut conts = HashMap::new();
    while let Some(now) = queue.pop_front() {
        val += now.1;
        if now.0 != low {
            queue.push_back(now);
        } else {
            items[low as usize] -= 1;
            if items[low as usize] == 0 {
                low -= 1
            }

            let cont = conts.entry(now.0).or_insert_with(Vec::new);
            if cont.is_empty() {
                cont.push(now.1);
            } else {
                for &i in cont.iter() {
                    if i < now.1 {
                        val += 2 * i
                    } else {
                        break;
                    }
                }
                cont.push(now.1);
                cont.sort_unstable();
            }
        }
    }
    writeln!(res,"{}",val).unwrap();
    print!("{}", res);
}

// 제출번호 : 88982698, 메모리 : 13224, 시간 : 0 