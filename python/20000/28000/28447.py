import sys
input = lambda: sys.stdin.readline().rstrip()

n,k = map(int,input().split())
mn = -100000
nli = [list(map(int,input().split())) for _ in range(n)]
vis = [0] * (k+1)

def dfs(st, ct):
    global mn

    if ct > k:
        return
    if st == n:
        if ct == k:
            nn = 0
            for i in range(ct):
                for j in range(i+1,ct):
                    nn += nli[vis[i]][vis[j]]
            mn = max(mn,nn)
        return
    vis[ct] = st
    dfs(st+1,ct+1)
    dfs(st+1,ct)

dfs(0,0)
print(mn)

# 제출 번호 : 96104533, 메모리 : 32412, 시간 : 36