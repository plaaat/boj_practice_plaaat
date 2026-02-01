import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = ((0,-1), (1,0), (-1,0), (0,1))
n, m = map(int,input().split())
vis = [[[[False] * m for _ in range(n)]for _ in range(m)] for _ in range(n)]

maps = [input() for _ in range(n)]

for i in range(n):
    for j in range(m):
        if maps[i][j] == 'R':
            rx, ry = j, i
        elif maps[i][j] == 'B':
            bx, by = j, i

q = deque()
vis[ry][rx][by][bx] = True
q.append((rx,ry,bx,by,0))

def mov(x,y,dx,dy):
    movd = 0
    while maps[y + dy][x + dx] != '#' and maps[y][x] != 'O':
        x += dx
        y += dy
        movd += 1
    
    return x,y,movd

res = 0
while q:
    nrx, nry, nbx, nby, dis = q.popleft()
    if dis == 10:
        break
    for dx, dy in d:
        nnrx,nnry,rmd = mov(nrx,nry,dx,dy)
        nnbx,nnby,bmd = mov(nbx,nby,dx,dy)
        if maps[nnby][nnbx] == 'O':
            continue
        if maps[nnry][nnrx] == 'O':
            q = deque([])
            res = 1
            break
        
        if nnrx == nnbx and nnry == nnby:
            if rmd < bmd:
                nnbx -= dx
                nnby -= dy
            else:
                nnrx -= dx
                nnry -= dy

        if not vis[nnry][nnrx][nnby][nnbx]:
            vis[nnry][nnrx][nnby][nnbx] = True
            q.append((nnrx,nnry,nnbx,nnby,dis+1))

print(res)

# 제출 번호: 102531528, 메모리 : 35044, 시간 : 60 