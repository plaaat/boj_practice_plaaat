import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

for _ in range(t):
    n, k = map(int,input().split())
    ctim = [0] + list(map(int,input().split()))
    kli = [[] for _ in range(n+1)]
    fro = [0] * (n+1)
    
    for _ in range(k):
        a, b = map(int, input().split())
        kli[a].append(b)
        fro[b] += 1
    
    w = int(input())
    dp = ctim.copy()
    q = deque([i for i in range(1, n+1) if not fro[i]])

    while q:
        now = q.popleft()
        for nxt in kli[now]:
            dp[nxt] = max(dp[nxt], dp[now] + ctim[nxt])
            fro[nxt] -= 1
            if not fro[nxt]:
                q.append(nxt)

    print(dp[w])

# 제출 번호 : 102090943, 메모리 : 37080, 시간 : 1264