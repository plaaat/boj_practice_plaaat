import sys
input = lambda: sys.stdin.readline().rstrip()

wo1 = input()
wo2 = input()

ln1 = len(wo1)
ln2 = len(wo2)

dp = [[0] * (ln2+1) for _ in range(ln1+1)]

for i in range(1, ln1+1):
    for j in range(1,ln2+1):
        if wo1[i-1] == wo2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])

res = ''
print(dp[ln1][ln2])

while ln1 > 0 and ln2 > 0:
    if wo1[ln1-1] == wo2[ln2-1]:
        res += wo1[ln1-1]
        ln1 -= 1
        ln2 -= 1
    else:
        if dp[ln1-1][ln2] > dp[ln1][ln2-1]:
            ln1 -= 1
        else:
            ln2 -= 1

print(res[::-1])

# 제출 번호 : 102087284, 메모리 : 56604, 시간 : 472