import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,k = map(int,input().split())
q = deque([])
q.append(n)
vis = [0]*100001
vis[n] = 1
while q:
    lo = q.popleft()
    lo2 = lo*2
    if lo2<100001 and not vis[lo2]:
        q.append(lo2)
        vis[lo2] = vis[lo]
    if lo-1>=0 and not vis[lo-1]:
        q.append(lo-1)
        vis[lo-1] = vis[lo]+1
    if lo+1<100001 and not vis[lo+1]:
        q.append(lo+1)
        vis[lo+1] = vis[lo]+1
print(vis[k]-1)

#....? 않이 +-를 바꾸니까 통과하네...