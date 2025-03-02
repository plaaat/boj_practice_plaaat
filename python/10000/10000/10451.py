import sys
input = lambda: sys.stdin.readline().rstrip()

t = int(input())
def find(now):
    vis[now] = 1
    if not vis[sli[now]]:
        find(sli[now])
    
for _ in range(t):
    n = int(input())
    sli = [0] + list(map(int,input().split()))
    ans = 0
    vis = [0] * (n+1)
    
    for i in range(1,n+1):
        if not vis[i]:
            find(i)
            ans += 1
    print(ans)