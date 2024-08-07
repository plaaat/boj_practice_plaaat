import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
le = {}
for _ in range(m):
  a,b = map(int,input().split())
  if a in le:
    le[a].append(b)
  else:
    le[a] = [b]
  if b in le:
    le[b].append(a)
  else:
    le[b] = [a]

mn = float('inf')
pn = 0
def bfs(a):
  q = deque([[a,0]])
  vis = [False]*(n+1)
  vis[a] = True
  tn = 0
  while q:
    x,num= q.popleft()
    tn+=num
    for i in le[x]:
      if not vis[i] and i in le:
        q.append([i,num+1])
        vis[i] = True
  return tn
for i in range(m):
  if i in le:
    tem = bfs(i)
    if tem < mn:
      pn = i
      mn = tem
print(pn)


#  제출 번호 : 79843472, 메모리 : 34072, 시간 : 112