import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

n, m = map(int, input().split())

stuli = [[] for  _ in range(n+1)]
for _ in range(m):
    a, b = map(int, input().split())
    stuli[a].append(b)

vis = set()
res = []

def dfs(x):
    vis.add(x)
    for i in stuli[x]:
        if not i in vis:
            dfs(i)
    res.append(x)

for i in range(1, n+1):
    if not i in vis:
        dfs(i)

print(*res[::-1])

# 제출 번호 : 102089484, 메모리 : 41628, 시간 : 184