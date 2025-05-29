import sys
from collections import deque

input = lambda: sys.stdin.readline().rstrip()

def sol(n,sx,sy,ex,ey):
    vis = [[False] * n for _ in range(n)]
    q = deque()
    vis[sy][sx] = True
    q.append((sx,sy,0))
    while q:
        nx,ny,c = q.popleft()
        if nx == ex and ny == ey:
            return c
        for dx,dy in d:
            dx += nx
            dy += ny
            if 0 <= dx < n and 0 <= dy < n and not vis[dy][dx]:
                vis[dy][dx] = True
                q.append((dx,dy,c+1))

d = [(1,2),(-1,2),(1,-2),(-1,-2),(2,1),(-2,1),(2,-1),(-2,-1)]
t = int(input())
for _ in range(t):
    n = int(input())
    sx,sy = map(int,input().split())
    ex,ey = map(int,input().split())
    print(sol(n,sx,sy,ex,ey))

# 제출 번호 : 94872052, 메모리 : 34984, 시간 : 980