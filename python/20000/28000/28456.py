import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n = int(input())
nli = [deque(map(int,input().split())) for _ in range(n)]

t = int(input())
top = 0
for _ in range(t):
    x = list(map(int,input().split()))
    if x[0] == 1:
        nli[x[1]-1].rotate(1)
    else:
        tli = [[0] * n for _ in range(n)]
        for i in range(n):
            for j in range(n):
                tli[j][n-i-1] = nli[i][j]
        nli = [deque(r) for r in tli]

for r in nli:
    print(*r)

# 제출 번호: 101217923, 메모리 : 34924, 시간 : 268