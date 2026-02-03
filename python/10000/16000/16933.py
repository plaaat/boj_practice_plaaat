import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

n, m, k = map(int, input().split())
d = [(1,0),(0,1),(-1,0),(0,-1)]

maps = [input() for _ in range(n)]

vis = [[-1] * m for _ in range(n)]
vis[0][0] = 0
q = deque([])
q.append((0,0,0,1,False))
res = -1

while q:
    nx,ny,rw,step,ntf = q.popleft()
    watf = False
    if nx == m-1 and ny == n-1:
        res = step
        break

    for dx,dy in d:
        tx = dx + nx
        ty = dy + ny
        if tx < 0 or tx >= m or ty < 0 or ty >= n:
            continue
        if vis[ty][tx] != -1 and vis[ty][tx] <= rw:
            continue
        if maps[ty][tx] == '1':
            if rw == k:
                continue
            if ntf:
                watf = True
                continue
            q.append((tx,ty,rw+1,step+1,True))
            vis[ty][tx] = rw+1
        else:
            vis[ty][tx] = rw
            q.append((tx,ty,rw,step+1,not ntf))
    if watf:
        q.append((nx,ny,rw,step+1,False))

print(res)

# 제출 번호 : 102596689, 메모리 : 260216, 시간 : 3044