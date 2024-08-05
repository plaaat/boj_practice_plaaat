import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

m,n = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
q = deque([])
dx,dy = [-1,1,0,0],[0,0,-1,1]
num = 0

for i in range(n):
  for s in range(m):
    if li[i][s] == 1:
      q.append([i,s])
def bfs():
  while q:
    x,y = q.popleft()
    for i in range(4):
      xx,yy = dx[i]+x, dy[i]+y
      if 0<=xx<n and 0<=yy<m and li[xx][yy] == 0:
        li[xx][yy] = li[x][y]+1
        q.append([xx,yy])
bfs()
tf = True
for i in li:
  if not tf:break
  for s in i:
    if s == 0:
      print(-1)
      tf = False
      break
  num = max(num,max(i))
if tf:print(num-1)#  제출 번호 : 79660079, 메모리 : 106728, 시간 : 1392