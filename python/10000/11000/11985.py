import sys
input = lambda: sys.stdin.readline().rstrip()

n,m,k = map(int,input().split())
val = [0] + [int(input()) for _ in range(n)]
dp = [float('inf')] * (n + 1)
dp[0] = 0


for i in range(1,n+1):
    ma,mi = 0,float('inf')
    for j in range(1, m+1):
        if i < j:break
        ma = max(ma, val[i - j + 1]) #마마..저슷킬더맨..
        mi = min(mi, val[i - j + 1])
        dp[i] = min(dp[i], dp[i - j] + k + j * (ma - mi))

print(dp[-1])

# 제출 번호 : 85493717, 메모리 : 111952, 시간 : 492  By.pypy3
