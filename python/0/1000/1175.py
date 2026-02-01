import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = ((0,1),(0,-1),(1,0),(-1,0))
n, m = map(int, input().split())

maps = [input() for _ in range(n)]
c1x, c1y = -1, -1
c2x, c2y = 0, 0
sx, sy = 0, 0

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'S':
            sx, sy = j, i
        elif maps[i][j] == 'C':
            if c1x == -1:
                c1x, c1y = j, i
            else:
                c2x, c2y = j, i

vis = [[[[False] * 4 for _ in range(m)] for _ in range(n)] for _ in range(3)]
q = deque([])
q.append((sx,sy,0,0,4))
res = -1
vis[0][sy][sx] = [True] * 4
vis[1][c1y][c1x] = [True] * 4
vis[2][c2y][c2x] = [True] * 4

while q:
    nx,ny,dis,visc,pred = q.popleft()
    if maps[ny][nx] == 'C':
        if visc != 0:
            res = dis
            break
        else:
            if nx == c1x and ny == c1y:
                visc = 1
            else:
                visc = 2
    for i in range(4):
        if i == pred:
            continue
        dx, dy = d[i]
        dx += nx
        dy += ny
        if 0 <= dx < m and 0 <= dy < n and not vis[visc][dy][dx][i]:
            if maps[dy][dx] == '#':
                continue
            vis[visc][dy][dx][i] = True
            q.append((dx, dy, dis+1, visc, i))

print(res)

# 제출 번호 : 102524622, 메모리 : 35256, 시간 : 120