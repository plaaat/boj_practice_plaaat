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
print(max(vis))#  ���� ��ȣ : 80017808, �޸� : 34016, �ð� : 176