use std::collections::HashSet;
use std::io;
use std::fmt::Write;

fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}

struct Finder {
    tree: Vec<i32>,
}

impl Finder {
    fn new(x:i32) -> Self {
        let tree = (0..=x).collect();
        Finder { tree }
    }
    
    fn findp(&mut self, x:i32) -> i32 {
        if self.tree[x as usize] == x {
            x
        } else {
            self.tree[x as usize] = self.findp(self.tree[x as usize]);
            self.tree[x as usize]
        }
    }
    
    fn cal(&mut self, mut a:i32, mut b:i32) {
        a = self.findp(a);
        b = self.findp(b);
        if a < b {
            self.tree[b as usize] = a;
        } else {
            self.tree[a as usize] = b;
        }
    }

    fn connecttf(&mut self, n: i32) -> bool {
        let root = self.findp(1);
        for i in 2..=n {
            if self.findp(i) != root {
                return false;
            }
        }
        true
    }
}

fn main() {
    let mut output = String::new();
    let inp1:String = input();
    let mut inp1 = inp1.split_ascii_whitespace();
    let (n,k):(i32,i32) = 
        (inp1.next().unwrap().parse().unwrap(),
         inp1.next().unwrap().parse().unwrap());
    
    let mut totco:i64 = 0;
    let mut find = Finder::new(n);
    let mut roads = Vec::new();
    let mut vis = HashSet::new();
    
    for _ in 0..k {
        let inp2 = input();
        let mut inp2 = inp2.split_ascii_whitespace();
        let (a,b,c) : (i32,i32,i64) = 
            (inp2.next().unwrap().parse().unwrap(),
             inp2.next().unwrap().parse().unwrap(),
             inp2.next().unwrap().parse().unwrap());
        vis.insert(a);
        vis.insert(b);
        totco += c;
        roads.push((c,a,b));
    }
    
    roads.sort();
    
    let mut costs:i64 = 0;
    for (c,a,b) in roads {
        if find.findp(a) != find.findp(b) {
            find.cal(a,b);
            costs += c;}}
        
    if !find.connecttf(n) || vis.len() != n as usize{
        writeln!(output,"-1").unwrap();
    } else {
        writeln!(output,"{}",totco - costs).unwrap();
    }

    print!("{}", output);
}

// 제출 번호 : 85983650, 메모리 : 26368, 시간 : 212