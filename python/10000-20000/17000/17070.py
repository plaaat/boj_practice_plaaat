import sys
sys.setrecursionlimit(10**5)
input = sys.stdin.readline

n = int(input())
li = [list(map(int, input().split())) for _ in range(n)]

xx, yy, zz = 0, 1, 2
dx = [0, 1, 1]
dy = [1, 0, 1]

vis = [[[-1] * 3 for _ in range(n)] for _ in range(n)]

def dfs(x, y, d):
    if x == n - 1 and y == n - 1:
        return 1
    
    if vis[x][y][d] != -1:
        return vis[x][y][d]
    
    count = 0
    for i in range(3):
        if (d == xx and i == yy) or (d == yy and i == xx):
            continue
        
        nx, ny = x + dx[i], y + dy[i]
        
        if 0 <= nx < n and 0 <= ny < n and li[nx][ny] == 0:
            if i == zz and (li[x+1][y] == 1 or li[x][y+1] == 1):
                continue
            count += dfs(nx, ny, i)
    
    vis[x][y][d] = count
    return count

result = dfs(0, 1, xx)
print(result)