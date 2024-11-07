<div align="center"> 

# 러스트 템플릿
</div>

* 아무리봐도 러스트를 통한 ps를 하기위해선 템플릿이 필요해 보인다.
* 그러니 만들어야징

## 목차
>1. [input](#input)
>2. [output](#output)
>3. [구조체 활용](#구조체-활용-dpdfsetc)
## Input
``` rust
fn input() -> String {
    let mut line = String::new();
    io::stdin().read_line(&mut line).unwrap();
    line.trim().to_string()
}
```

## Output
``` rust
let mut output = String::new();

/*코드*/

writeln!(output,"{}",/*결과*/).unwrap();

print!("{}",output);
```

## 구조체 활용 (dp,dfs,etc...)
>[15989](./10000/15000/15989.rs) dp 활용 문제에서 사용 
```rust
struct Finder {
    dp: HashMap<i32,i32>,
}
/*구조체에 타입명시 및 구조체 내부공유 */
impl Finder {
    fn new() -> Self {
        let mut dp = HashMap::new();
        dp.insert(1, 1);
        dp.insert(2, 2);
        dp.insert(3, 3);
        Finder { dp }
    }
    /*Finder()::new() 로 dp hashmap 생성*/
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

```