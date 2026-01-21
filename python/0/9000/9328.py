import sys
input = lambda: sys.stdin.readline().rstrip()
from collections import deque

d = [(0,-1), (1,0), (-1,0), (0,1)]

t = int(input())

for _ in range(t):
    h, w = map(int, input().split())
    maps = ['.' * (w+2)] + ['.'+input()+'.' for _ in range(h)]+['.' * (w+2)]
    w += 2
    h += 2
    vis = [[False] * w for _ in range(h)]
    key = input()
    keys = set()
    if key != '0':
        for k in key:
            keys.add(chr(ord(k)-32))

    q = deque([])
    res = 0
    locked = {}
    q.append((0,0))
    vis[0][0] = True
    while q:
        nx, ny = q.popleft()
        for dx, dy in d:
            dx += nx
            dy += ny
            if not (0 <= dx < w and 0 <= dy < h):
                continue
            if vis[dy][dx]:
                continue
            
            noww = maps[dy][dx]
            if noww == '*':
                continue
            if noww == '.' or noww == '$' or noww in keys:
                if noww == '$':
                    res += 1
                vis[dy][dx] = True
                q.append((dx,dy))
            elif noww.isalpha():
                if noww.islower():
                    keys.add(chr(ord(noww)-32))
                    vis[dy][dx] = True
                    q.append((dx,dy))
                    if chr(ord(noww)-32) in locked:
                        for lx,ly in locked[chr(ord(noww)-32)]:
                            q.append((lx,ly))
                            vis[ly][lx] = True
                        del locked[chr(ord(noww)-32)]
                else:
                    if not noww in locked:
                        locked[noww] = []
                    locked[noww].append((dx,dy))
        
    print(res)

# 제출 번호 : 102167678, 메모리 : 35044, 시간 : 180