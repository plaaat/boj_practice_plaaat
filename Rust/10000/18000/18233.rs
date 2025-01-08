use std::{fmt::Write, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn dfs(vis: usize, s: usize, n: usize, p: usize, e: i32, arr: &Vec<(i32,i32)>, visit: &mut Vec<usize>, pli: &mut Vec<i32>, flag: &mut bool) {
    if *flag {
        return;
    }

    if vis != p {
        for i in s..n {
            visit[vis] = i;
            dfs(vis + 1, i + 1, n, p, e, arr, visit, pli, flag);
            if *flag {
                return;
            }
        }
    } else {
        let mut min = 0;
        let mut max = 0;

        for &idx in visit.iter().take(p) {
            min += arr[idx].0;
            max += arr[idx].1;
        }

        if e < min || max < e {
            return;
        }

        *flag = true;
        let mut diff = e - min;

        for &idx in visit.iter().take(p) {
            pli[idx] += arr[idx].0;
            if diff != 0 {
                let still = arr[idx].1 - arr[idx].0;
                if still < diff {
                    pli[idx] += still;
                    diff -= still;
                } else {
                    pli[idx] += diff;
                    diff = 0;
                }
            }
        }
    }
}

fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp1: Vec<i32> = inp1.split_whitespace().map(|x| x.parse().unwrap()).collect();

    let (n, p, e) = (inp1[0] as usize, inp1[1] as usize, inp1[2]);

    let mut nli = Vec::new();
    let mut pli = vec![0; n];
    let mut vis = vec![0; p];
    let mut flag = false;

    for _ in 0..n {
        let inp2 = input();
        let inp2: Vec<i32> = inp2.split_whitespace().map(|x| x.parse().unwrap()).collect();
        nli.push((inp2[0],inp2[1]));
    }

    dfs(0, 0, n, p, e, &nli, &mut vis, &mut pli, &mut flag);

    if flag {
        writeln!(res,"{}", pli.iter().map(|x| x.to_string()).collect::<Vec<String>>().join(" ")).unwrap();
    } else {
        writeln!(res,"-1").unwrap();
    }
    print!("{}", res);
}

// 제출번호 : 88225084, 메모리 : 13216, 시간 : 8