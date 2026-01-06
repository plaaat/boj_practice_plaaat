import sys
input = lambda: sys.stdin.readline().rstrip()

c,n = map(int,input().split())
city = []
dp = [float('inf')] * (c+101)
for _ in range(n):
    w,v = map(int, input().split())
    city.append((w,v))

dp[0] = 0

res = float('inf')
for wei, val in city:
    for v in range(val,c+101):
        dp[v] = min(dp[v],dp[min(c,v-val)] + wei)
        if v >= c:
            res = min(res,dp[v])

print(res)

# 제출 번호 : 101670688, 메모리 : 32412, 시간 : 44