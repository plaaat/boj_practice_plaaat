import sys
input = lambda: sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)

t = int(input())

for _ in range(t):
    n = int(input())
    nli = [0] + list(map(int,input().split()))
    vis = [False] * (n+1)
    endli = [False] * (n+1)
    res = 0

    def dfs(now):
        global res

        vis[now] = True
        nxt = nli[now]

        if not vis[nxt]:
            dfs(nxt)
        elif not endli[nxt]:
            tmp = nxt
            cycle = 1
            while tmp != now:
                cycle += 1
                tmp = nli[tmp]
            res += cycle
        
        endli[now] = True
    
    for i in range(1,n+1):
        if not vis[i]:
            dfs(i)
    
    print(n - res)

# 제출 번호 : 102438484, 메모리 : 59392, 시간 : 2340