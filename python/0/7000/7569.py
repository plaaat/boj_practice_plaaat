import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

m,n,h = map(int,input().split())
li = [[list(map(int,input().split())) for _ in range(n)] for _ in range(h)]
q = deque([])
dx,dy,dz = [-1,1,0,0,0,0],[0,0,-1,1,0,0],[0,0,0,0,-1,1]
num = 0

for j in range(h):
  for i in range(n):
    for s in range(m):
      if li[j][i][s] == 1:
        q.append([i,s,j])

def bfs():
  while q:
    x,y,z = q.popleft()
    for i in range(6):
      xx,yy,zz = dx[i]+x, dy[i]+y, dz[i]+z
      if 0<=xx<n and 0<=yy<m and 0<=zz<h and li[zz][xx][yy] == 0:
        li[zz][xx][yy] = li[z][x][y]+1
        q.append([xx,yy,zz])
bfs()
tf = True

for i in li:
  if not tf:break
  for s in i:
    if not tf:break
    for j in s:
      if j == 0:
        print(-1)
        tf = False
        break
    num = max(num,max(s))
if tf:print(num-1)#  제출 번호 : 79646717, 메모리 : 52532, 시간 : 1904