import sys
input = lambda: sys.stdin.readline().rstrip()
import heapq

n, m = map(int, input().split())
nli = [[] for _ in range(n+1)]
deg = [0] * (n+1)

for _ in range(m):
    a, b = map(int, input().split())
    deg[b] += 1
    nli[a].append(b)

q = [i for i in range(1,n+1) if not deg[i]]
res = []

while q:
    now = heapq.heappop(q)
    res.append(now)

    for nxt in nli[now]:
        deg[nxt] -= 1
        if deg[nxt] == 0:
            heapq.heappush(q,nxt)

print(*res)

# 제출 번호 : 102092767, 메모리 : 41656, 시간 : 200