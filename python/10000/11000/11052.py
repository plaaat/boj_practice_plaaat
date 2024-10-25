import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
val = [0] + list(map(int,input().split()))
vis = [0] * (n + 1)

for i in range(1,n+1):
    for j in range(1,i+1):
        if not vis[i]:
            vis[i] = vis[i-j] + val[j]
        else:
            vis[i] = max(vis[i],vis[i-j]+val[j])
print(vis[-1])

# 제출 번호 : 85617624, 메모리 : 31120, 시간 : 236
