import sys
input = lambda:sys.stdin.readline().rstrip()

n,k = map(int,input().split())
dp = [[0]*(k+1) for _ in range(n+1)]
li = [list(map(int,input().split())) for _ in range(n)]

for i in range(n):
    for j in range(1,k+1):
        if li[i][0] <= j:
            dp[i+1][j] = max(li[i][1]+dp[i][j-li[i][0]],dp[i][j])
        else:
            dp[i+1][j] = dp[i][j]
print(dp[-1][-1])#  제출 번호 : 80550090, 메모리 : 189776, 시간 : 352