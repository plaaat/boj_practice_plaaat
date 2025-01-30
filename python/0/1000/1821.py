import sys
input = lambda: sys.stdin.readline().rstrip()

def dfs(a, b):
    global tf
    if tf or b > target_sum:
        return
    if a == n:
        if b == target_sum:
            for i in range(n):
                print(ans[i], end=" ")
            tf = 1
        return
    for i in range(1, n + 1):
        if not check[i]:
            check[i] = 1
            ans[a] = i
            dfs(a + 1, b + mul[a] * i)
            if tf:
                break
            check[i] = 0

n, target_sum = map(int, input().split())
fac = [0] * n
mul = [0] * n
check = [0] * (n + 1)
ans = [0] * n

fac[0] = 1
for i in range(1, n):
    fac[i] = fac[i-1] * i

for i in range(n):
    mul[i] = fac[n - 1] // (fac[n - 1 - i] * fac[i])

tf = 0
dfs(0, 0)



#  제출 번호 : 83997527, 메모리 : 31120, 시간 : 56