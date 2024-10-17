import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

def bfs(cost,wb):
    vis = [0] * n
    q = deque()
    q.append((0,wb))
    vis[0] = 1
    pn = cost[0][wb]
    
    while q:
        now,wb = q.popleft()
        wb = 0 if wb else 1
        if not now in tree:continue
        for row in tree[now]:
            if not vis[row]:
                vis[row] = 1
                pn += cost[row][wb]
                q.append((row,wb))
    return pn

n = int(input())
tree = {}
tree[0] = []

for _ in range(n-1):
    a,b = map(int,input().split())
    if not b in tree:tree[b] = []
    if not a in tree:tree[a] = []
    tree[a].append(b)
    tree[b].append(a)

cost = [list(map(int,input().split())) for _ in range(n)]

print(min(bfs(cost,1),bfs(cost,0)))

# 제출 번호 : 85221021, 메모리 : 78044, 시간 : 644
