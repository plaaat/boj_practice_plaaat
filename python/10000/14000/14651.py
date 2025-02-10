import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
dp = [0 for _ in range(n + 1)]
dp[2] = 2

for i in range(3,n + 1):
    dp[i] = (dp[i - 1] * 3) % 1000000009
print(dp[n])

# 제출번호 : 89870407, 메모리 : 33432, 시간 : 40