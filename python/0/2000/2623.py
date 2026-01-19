import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n, m = map(int,input().split())
pli = [[] for _ in range(n+1)]
deg = [0] * (n+1)

for _ in range(m):
    tli = list(map(int, input().split()))
    for i in range(1,tli[0]):
        deg[tli[i+1]] += 1
        pli[tli[i]].append(tli[i+1])

q = deque([i for i in range(1,n+1) if not deg[i]])
res = []

while q:
    now = q.popleft()
    res.append(now)
    
    for x in pli[now]:
        deg[x] -= 1
        if not deg[x]:
            q.append(x)

if len(res) == n:
    print(*res, sep='\n')
else:
    print(0)

# 제출 번호 : 102091851, 메모리 : 34944, 시간 : 60