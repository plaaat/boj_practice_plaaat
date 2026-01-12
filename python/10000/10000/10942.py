import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [[0] * n for _ in range(n)]
nli = tuple(map(int,input().split()))

for i in range(n-1):
    dp[i][i] = 1
    if nli[i] == nli[i+1]:
        dp[i][i+1] = 1

dp[n-1][n-1] = 1

for i in range(2, n):
    for j in range(n-i):
        k = j + i
        if nli[j] == nli[k] and dp[j+1][k-1]:
            dp[j][k] = 1

m = int(input())
for _ in range(m):
    a,b = map(int,input().split())
    print(dp[a-1][b-1])

# 제출 번호 : 101857190, 메모리 : 63888, 시간 : 2176