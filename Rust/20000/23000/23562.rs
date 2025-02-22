use std::{fmt::Write, i32, io::{self, BufRead}};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}


fn cal(mut cost:i32,mut midtf:bool,mut x:i32,mut y:i32,k:i32,stx:i32,sty:i32,maps:&Vec<Vec<char>>,a:i32,b:i32) -> i32 {
    let n = maps.len() as i32;
    let m = maps[0].len() as i32;
    
    if (x - stx == k * 3 - 1) && (y - sty == k * 3 - 1) {
        if maps[y as usize][x as usize] == '.' {
            cost += a
        }
        for tx in 0..m {
            for ty in 0..n {
                if stx <= tx && tx <= x && sty <= ty && ty <= y {
                    continue;
                }
                if maps[ty as usize][tx as usize] == '#' {
                    cost += b
                }
            }
        }
        return cost
    } else {
        if !midtf {
            if maps[y as usize][x as usize] == '.' {
                cost += a
            }
            x += 1;
            if x - stx == k * 3 {
                x = stx;
                y += 1;
                if y - sty == k {
                    midtf = true
                }
            }
        } else {
            if x - stx < k {
                if maps[y as usize][x as usize] == '.' {
                    cost += a
                }
                x += 1
            } else {
                if maps[y as usize][x as usize] == '#' {
                    cost += b
                }
                x += 1;
                if x - stx == k * 3 {
                    x = stx;
                    y += 1;
                    if y - sty == k * 2 {
                        midtf = false
                    }
                }
            }
        }
        if x == m {return i32::MAX;}
        if y == n {return i32::MAX;}
        return cal(cost,midtf,x,y,k,stx,sty,maps,a,b);
    }
}


fn main() {
    let mut res = String::new();
    let inp1 = input();
    let inp2 = input();
    let inp1:Vec<i32> = inp1.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (n,m) = (inp1[0],inp1[1]);
    let inp2:Vec<i32> = inp2.split_ascii_whitespace().map(|x| x.parse().unwrap()).collect();
    let (a,b) = (inp2[0],inp2[1]);
    
    let mut maps = Vec::with_capacity(n as usize);
    for _ in 0..n {
        let inp3:Vec<char> = input().chars().collect();
        maps.push(inp3)
    }
    let mut ans = i32::MAX;
    for i in 1..7 {
        for x in 0..m {
            for y in 0..n {
                ans = ans.min(cal(0,false,x,y,i,x,y,&maps,a,b))
            }
        }
    }
    writeln!(res,"{ans}").unwrap();
    print!("{res}")
}

// 제출 번호 : 89997106, 메모리 : 13212, 시간 : 4