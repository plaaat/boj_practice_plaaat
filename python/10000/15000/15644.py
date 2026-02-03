import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m = map(int, input().split())
d = [(1,0,'R'),(0,1,'D'),(-1,0,'L'),(0,-1,'U')]

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
q.append((rx, ry, bx, by, 0, ''))
res = 0
resw = ''
counter = lambda x,y,nex,ney: abs(nex - x) + abs(ney - y)

while q:
    nrx, nry, nbx, nby, nty, nmv = q.popleft()

    if nty > 10:
        res = -1
        break
    fl = False

    for dx,dy,dw in d:
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
            resw = nmv+dw
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
        if not (rtx,rty,btx,bty) in vis:
            q.append((rtx,rty,btx,bty,nty+1,nmv+dw))
            vis.add((rtx,rty,btx,bty))
    if fl:
        break

if res == 0 or res > 10:
    res = -1
    resw = ''

print(res)
if resw:
    print(resw)

# 제출 번호 : 102594099, 메모리 : 35076, 시간 : 60