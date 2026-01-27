import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = [(0,-1),(-1,0),(0,1),(1,0)]
n = int(input())

maps = []

sx,sy = -1, -1
for i in range(n):
    inp = list(map(int,input().split()))
    maps.append(inp)
    if sx != -1:continue
    for j in range(n):
        if inp[j] == 9:
            sx = j
            sy = i
            maps[sy][sx] = 0
            break

res = 0
siz = 2
sta = 0

while True:
    vis = [[False] * n for _ in range(n)]
    q = deque([])
    vis[sy][sx] = True
    tli = []
    q.append((sx,sy,0))
    mind = float('inf')

    while q:
        nx,ny,nowd = q.popleft()
        if nowd + 1 > mind:
            break
        for dx, dy in d:
            dx += nx
            dy += ny
            if 0 <= dx < n and 0 <= dy < n and not vis[dy][dx] and maps[dy][dx] <= siz:
                vis[dy][dx] = True
                if 0 < maps[dy][dx] < siz:
                    tli.append((dy, dx))
                    mind = nowd + 1
                else:
                    q.append((dx,dy,nowd+1))

    
    if not tli:
        break
    
    tli.sort()
    ny,nx = tli[0]
    res += mind
    maps[sy][sx] = 0
    maps[ny][nx] = 0
    sta += 1
    sx,sy = nx, ny
    
    if sta == siz:
        siz += 1
        sta = 0
    
print(res)

# 제출 번호 : 102368507, 메모리 : 35004, 시간 : 52