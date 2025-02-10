import sys
sys.setrecursionlimit(10**6)
input = lambda: sys.stdin.readline().rstrip()

def dfs(depth, r):
    if not r in graph:
        return
    graph[r].sort()
    for i in graph[r]:
        if visit[i] == -1:
            visit[i] = depth
            dfs(depth+1,i)

n,m,r = map(int,input().split())
graph = {}

for _ in range(m):
    u,v = map(int,input().split())
    if u in graph:
        graph[u].append(v)
    else:
        graph[u] = [v]
    if v in graph:
        graph[v].append(u)
    else:
        graph[v] = [u]

visit = [-1] * (n + 1)
visit[r] = 0
dfs(1,r)
for i in visit[1:]:
    print(i)


# 제출 번호 : 89499382, 메모리 : 79292, 시간 : 724
