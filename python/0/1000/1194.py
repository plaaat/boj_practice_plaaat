import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = ((0,-1), (1,0), (-1,0), (0,1))


n, m = map(int, input().split())
maps = [input() for _ in range(n)]

vis = [[[False] * 64 for _ in range(m)] for _ in range(n)]

q = deque([])
res = -1

for i in range(n):
    for j in range(m):
        if maps[i][j] == '0':
            sx, sy = j, i
            break
q.append((sx,sy,0,0))
vis[sy][sx][0] = True

while q:
    nx, ny, sta, dis = q.popleft()
    if maps[ny][nx] == '1':
        res = dis
        break
    if maps[ny][nx].islower():
        sta |= (1 << (ord(maps[ny][nx]) - 97))
    
    for dx, dy in d:
        dx += nx
        dy += ny
        if 0 <= dx < m and 0 <= dy < n and not vis[dy][dx][sta] and maps[dy][dx] != '#':
            if maps[dy][dx].isupper() and sta & 2 ** (ord(maps[dy][dx]) - 65) == 0:
                continue
            vis[dy][dx][sta] = True
            q.append((dx,dy,sta,dis+1))

print(res)

# 제출 번호 : 102526858, 메모리 : 35588, 시간 : 116