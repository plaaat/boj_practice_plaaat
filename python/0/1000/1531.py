import sys

input = sys.stdin.readline

n, m = map(int, input().split())
li = [[0] * 101 for _ in range(101)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    li[b-1][a-1] += 1
    li[d][c] += 1
    li[b-1][c] -= 1
    li[d][a-1] -= 1

for i in range(101):
    for j in range(1, 101):
        li[i][j] += li[i][j-1]

for j in range(101):
    for i in range(1, 101):
        li[i][j] += li[i-1][j]

num = sum(1 for i in range(100) for j in range(100) if li[i][j] > m)

print(num)


# 제출 번호 : 82288746 메모리 : 31120 시간 : 40