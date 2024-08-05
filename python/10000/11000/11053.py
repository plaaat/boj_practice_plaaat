import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = int(input())
li = list(map(int,input().split()))
vis = [1]*(n+1)

for i in range(n):
    for s in range(i):
        if li[i]>li[s]:
            vis[i] = max(vis[i],vis[s]+1)
print(max(vis))#  제출 번호 : 80017808, 메모리 : 34016, 시간 : 176