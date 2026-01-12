import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n,r,q = map(int,input().split())

tree = [[] for _ in range(n)]

for _ in range(n-1):
    u, v = map(int,input().split())
    u -= 1
    v -= 1
    tree[u].append(v)
    tree[v].append(u)

vis = [False for _ in range(n)]
dis = [0 for _ in range(n)]

def dfs(x):
    vis[x] = True
    dis[x] = 1

    for i in tree[x]:
        if not vis[i]:
            dfs(i)
            dis[x] += dis[i]

dfs(r - 1)

for _ in range(q):
    print(dis[int(input()) - 1])

# 제출 번호 : 101824885, 메모리 : 68568, 시간 : 372