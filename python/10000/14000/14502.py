import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque
from itertools import combinations

d = ((0,1),(1,0),(0,-1),(-1,0))
n, m = map(int,input().split())

li = [list(map(int,input().split())) for _ in range(n)]
vli = []
swli = []

for i in range(n):
    for j in range(m):
        if li[i][j] == 0:
            swli.append((j,i))
        elif li[i][j] == 2:
            vli.append((j,i))

sfln = len(swli)
res = -1

for w in combinations(swli,3):
    vis = [[False] * m for _ in range(n)]
    for j,i in w:
        vis[i][j] = True
    q = deque(vli)
    for j, i in vli:
        vis[i][j] = True
    virc = 0

    while q:
        nx,ny = q.popleft()
        for dx,dy in d:
            dx += nx
            dy += ny
            if 0 <= dx < m and 0 <= dy < n:
                if not vis[dy][dx] and li[dy][dx] == 0:
                    vis[dy][dx] = True
                    q.append((dx,dy))
                    virc += 1
        if sfln - 3 - virc <= res:
            break
    res = max(res,sfln-3-virc)

print(res)

# 제출 번호 : 102935344, 메모리 : 34992, 시간 : 3080