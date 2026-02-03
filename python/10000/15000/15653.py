import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
d = [(1,0),(0,1),(-1,0),(0,-1)]

vis = set()
maps = []

for i in range(n):
    inp1 = input()
    tma = []
    for j in range(m):
        x = inp1[j]
        tma.append(x)
        if x == 'R':
            rx, ry = j, i
        elif x == 'B':
            bx, by = j, i
    maps.append(tma)

q = deque([])
q.append((rx, ry, bx, by, 0))
res = 0

counter = lambda x,y,nex,ney: abs(nex - x) + abs(ney - y)

while q:
    nrx, nry, nbx, nby, nty = q.popleft()
    fl = False

    for dx,dy in d:
        rtx, rty, btx, bty = nrx, nry, nbx, nby
        while maps[rty + dy][rtx + dx] != '#' and maps[rty][rtx] != 'O':
            rtx += dx
            rty += dy
        while maps[bty + dy][btx + dx] != '#' and maps[bty][btx] != 'O':
            btx += dx
            bty += dy

        if maps[bty][btx] == 'O':
            continue
        if maps[rty][rtx] == 'O':
            res = nty + 1
            fl = True
            break

        if rtx == btx and rty == bty:
            rc = counter(nrx,nry,rtx,rty)
            bc = counter(nbx,nby,btx,bty)
            if rc > bc:
                rtx -= dx
                rty -= dy
            else:
                btx -= dx
                bty -= dy
        if (nrx,nry,nbx,nby) == (rtx,rty,btx,bty):
            continue
        if not (rtx,rty,btx,bty) in vis:
            q.append((rtx,rty,btx,bty,nty+1))
            vis.add((rtx,rty,btx,bty))
    if fl:
        break

if res == 0:
    res = -1

print(res)

# 제출번호 : 102594305, 메모리 : 35044, 시간 : 64