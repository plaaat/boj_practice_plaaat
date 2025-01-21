use std::{
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
    let mut map = vec![vec![0;1001];1001];

    let t = input().parse().unwrap();
    for i in 1..=t {
        let inp1 = input();
        let inp1: Vec<usize> = inp1.split_ascii_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let (x1,y1,mut x2,mut y2) = (inp1[0], inp1[1], inp1[2], inp1[3]);
        x2 += x1;
        y2 += y1;

        for x in x1..x2 {
            for y in y1..y2 {
                map[y][x] = i
            }
        }
    }

    let mut prli = vec![0;t as usize];
    for ma in map {
        for m in ma {
            if m != 0 {
                prli[m as usize - 1] += 1
            }
        }
    }

    for i in prli {
        writeln!(res,"{}",i).unwrap();
    }
    print!("{}",res)
}

// 내가 짠 코드... 겁나 비효율적이야 ㅋㅁㅋㅁㅋ...
// 제출번호 : 87378973, 메모리 : 17040, 시간 : 148

/* 
use std::{
    collections::HashMap,
    io::{self, BufRead},
};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn main() {
    let t: usize = input().parse().unwrap();

    let mut rectangles = Vec::with_capacity(t);
    for _ in 0..t {
        let inp: Vec<usize> = input()
            .split_ascii_whitespace()
            .map(|x| x.parse().unwrap())
            .collect();
        let (x1, y1, x2, y2) = (inp[0], inp[1], inp[2] + inp[0], inp[3] + inp[1]);
        rectangles.push((x1, y1, x2, y2));
    }

    let mut area_count = vec![0; t];
    let mut map: HashMap<(usize, usize), usize> = HashMap::new();

    for (i, &(x1, y1, x2, y2)) in rectangles.iter().enumerate() {
        for x in x1..x2 {
            for y in y1..y2 {
                map.insert((x, y), i);
            }
        }
    }

    for &index in map.values() {
        area_count[index] += 1;
    }

    for count in area_count {
        println!("{}", count);
    }
} */
// GPT 업데이트 테스트
// GPT 틀림 ㅋㅋ
