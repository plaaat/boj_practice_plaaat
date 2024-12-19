use std::io::{self, BufRead};

fn input() -> String {
    let stdin = io::stdin();
    let mut line = String::new();
    stdin.lock().read_line(&mut line).unwrap();
    line.trim().to_string()
}

fn gcd(mut a: i64, mut b: i64) -> i64 {
    while b != 0 {
        let temp = b;
        b = a % b;
        a = temp;
    }
    a
}

fn main() {
    let inp1 = input();
    let mut inp1 = inp1.split('.');
    let mut ja: i64 = inp1.next().unwrap().parse().unwrap();

    if let Some(wo) = inp1.next() {
        let mut mo = 1;

        if let Some(wo_inner) = wo.strip_suffix(')') {
            let parts: Vec<&str> = wo_inner.split('(').collect();
            let fir = parts[0];
            let sec = parts[1];

            if !fir.is_empty() {
                let firn = fir.parse::<i64>().unwrap();
                mo *= 10_i64.pow(fir.len() as u32);
                ja = ja * mo + firn;
            }

            let secn = sec.parse::<i64>().unwrap();
            let sec_mo = 10_i64.pow(sec.len() as u32) - 1;
            mo *= sec_mo;
            ja = ja * sec_mo + secn;
        } else {
            mo *= 10_i64.pow(wo.len() as u32);
            ja = mo * ja + wo.parse::<i64>().unwrap();
        }

        let gcd = gcd(ja, mo);
        ja /= gcd;
        mo /= gcd;
        println!("{}/{}", ja, mo);
    } else {
        println!("{}/1", ja);
    }
}

//제출 번호 : 87485268, 메모리 : 13208, 시간 : 0