import sys
input = lambda:sys.stdin.readline().rstrip()

n, m = map(int, input().split())
li = [list(map(int, input().split())) for _ in range(n)]
vis = [[False] * m for _ in range(n)]
d = ((1, 0), (-1, 0), (0, 1), (0, -1))
pn = 0

def dfs(x, y, depth, sum_value):
    global pn
    if depth == 4:
        pn = max(pn, sum_value)
        return
    
    for dx, dy in d:
        xx, yy = x + dx, y + dy
        if 0 <= xx < m and 0 <= yy < n and not vis[yy][xx]:
            vis[yy][xx] = True
            dfs(xx, yy, depth + 1, sum_value + li[yy][xx])
            vis[yy][xx] = False

def fu(x, y):
    total = li[y][x]
    min_val = float('inf')
    wings = 0
    for dx, dy in d:
        xx, yy = x + dx, y + dy
        if 0 <= xx < m and 0 <= yy < n:
            total += li[yy][xx]
            min_val = min(min_val, li[yy][xx])
            wings += 1
    if wings == 4:
        return total - min_val
    elif wings == 3:
        return total
    return -1

for i in range(n):
    for j in range(m):
        vis[i][j] = True
        dfs(j, i, 1, li[i][j])
        vis[i][j] = False
        pn = max(pn, fu(j, i))

print(pn)
#  제출 번호 : 79924299, 메모리 : 38000, 시간 : 4836