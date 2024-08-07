import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = []
vis = []
pli = []
for i in range(n):
  ili = tuple(map(int,input().split()))
  li.append(ili)
  if 2 in ili:
    lo2 = (i,ili.index(2))
  pli.append([-1]*m)
  vis.append([0]*m)
x = [0,0,1,-1]
y = [1,-1,0,0]

def bfs(a,b):
  que = deque()
  que.append((a,b,1))
  vis[b][a]+=1
  pli[b][a]+=1
  
  while que:
    t = que.popleft()
    loc = t[2]
    for i in range(4):
      xx,yy = t[0]+x[i], t[1]+y[i]
      if xx>-1 and xx<m and yy>-1 and yy<n and vis[yy][xx] == 0:
        if li[yy][xx]!=0:
          vis[yy][xx]+=1
          pli[yy][xx]+=loc+1
          que.append((xx,yy,loc+1))
bfs(lo2[1],lo2[0])

for i in range(n):
  for s in range(m):
    if not li[i][s]:
      pli[i][s] = 0
  print(*pli[i])


#  제출 번호 : 79646767, 메모리 : 41800, 시간 : 508