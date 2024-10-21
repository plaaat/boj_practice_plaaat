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

# 안제출함 16194랑 똑같. 사실 기초적 dp문제는 다 똑같지안나..