import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = ((0,-1), (1,0), (-1,0), (0,1))

while True:
    w, h = map(int,input().split())
    if w == 0:
        break
    maps = [input() for _ in range(h)]
    dirt = 0
    dirtm = [[0] * w for _ in range(h)]
    for i in range(h):
        for j in range(w):
            if maps[i][j] == 'o':
                sx, sy = j, i
            elif maps[i][j] == '*':
                dirt += 1
                dirtm[i][j] = dirt
    
    vis = [[[False] * (2 ** (dirt)) for _ in range(w)] for _ in range(h)]
    vis[sy][sx][0] = True
    q = deque([])
    q.append((sx,sy,0,0))
    res = -1

    while q:
        nx,ny,sta,dis = q.popleft()
        if dirtm[ny][nx] != 0:
            sta |= (1 << (dirtm[ny][nx]-1))
            vis[ny][nx][sta] = True
        if sta == (2 ** (dirt)) - 1:
            res = dis
            break
        
        for dx, dy in d:
            dx += nx
            dy += ny
            if 0 <= dx < w and 0 <= dy < h and not vis[dy][dx][sta] and not maps[dy][dx] == 'x':
                vis[dy][dx][sta] = True
                q.append((dx,dy,sta,dis+1))
    print(res)

# 제출 번호 : 102528154, 메모리 : 35804, 시간 : 1592