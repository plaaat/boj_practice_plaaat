import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = []
tf = 0
for i in range(n):
    tl = input()
    for j in range(n):
        if not tf and tl[j] == 'F':
            sx,sy = j,i
            tf = 1
    li.append(tl)

pn = 0
vis = set()
d = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1))
q = deque()
q.append((sx,sy))

while q:
    x,y = q.popleft()
    for dx,dy in d:
        dx += x
        dy += y
        if 0 <= dx < n and 0 <= dy < n and li[dy][dx] == '.' and not (dx,dy) in vis:
            vis.add((dx,dy))
            q.append((dx,dy))
            pn += 1
print(pn)
exit(0)
# 제출번호 : 84824870, 메모리 : 447836, 시간 : 4236  By.pypy3

# Claude로 이전 제출 최적화한버전

import sys
input = sys.stdin.readline

n = int(input())
grid = [input().rstrip() for _ in range(n)]

# 시작점 찾기
sx, sy = next((j, i) for i, row in enumerate(grid) for j, cell in enumerate(row) if cell == 'F')

# BFS 탐색
visited = [[False] * n for _ in range(n)]
visited[sy][sx] = True
queue = [(sx, sy)]
count = 0

directions = ((-1,-1),(-1,0),(-1,1),(1,-1),(1,0),(1,1),(0,-1))

for x, y in queue:
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < n and 0 <= ny < n and grid[ny][nx] == '.' and not visited[ny][nx]:
            visited[ny][nx] = True
            queue.append((nx, ny))
            count += 1

print(count)

# 제출 번호 : 84825035,  메모리 : 345080, 시간 : 1296 By.pypy3