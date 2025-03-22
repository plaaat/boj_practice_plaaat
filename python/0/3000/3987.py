import sys
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())

vis = {}
vist = {}
maps = []
for _ in range(n):
    maps.append(input())
sx,sy = map(int,input().split())

res,mn = '',-1

def dfs(x,y,d,t,st):
    global vis
    global vist
    dx,dy = d
    if maps[y][x] == 'C':
        return t
    if (x,y) in vist:
        if d in vist[(x,y)]:
            if vist[(x,y)][d] >= t:
                return -1
            else:
                vist[(x,y)][d] = t
        if st in vis[(x,y)]:
            if d in vis[(x,y)][st]:
                vist[(x,y)][d] = float('inf')
                return float('inf')
            else:
                vis[(x,y)][st][d] = t
    else:
        vist[(x,y)] = {d:t}
        vis[(x,y)][st] = {d:t}
    if maps[y][x] == '.':
        if y+dy == -1 or y + dy == n:
            return t
        if x + dx == -1 or x + dx == m:
            return t
        return dfs(x + dx, y + dy,d,t,st)
    
    if maps[y][x] == '/':
        if d == (-1,0):
            return dfs(x + dx,y + dy,(0,-1),t + 1,st)
        elif d == (1,0):
            return '?'