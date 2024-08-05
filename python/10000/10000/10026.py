import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
li = [list(input()) for i in range(n)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
vis1 = [[True] * n for _ in range(n)]
def bfs(a,b,c):
  q = deque([(a,b)])
  vis1[a][b] = False
  while q:
    x,y = q.popleft()
    for i in d:
      xx = x+i[0]
      yy = y+i[1]
      if 0<=xx<n and 0<=yy<n and vis1[xx][yy]:
        if c == li[xx][yy]:
          q.append([xx,yy])
          vis1[xx][yy] = False
c1 = 0
c2 = 0
for i in range(n):
  for j in range(n):
    if vis1[i][j]:
      color = li[i][j]
      bfs(i, j, color)
      c1 += 1
for i in range(n):
	for j in range(n):
	  if li[i][j] == 'G':
	    li[i][j] = 'R'
vis1 = [[True] * n for _ in range(n)]
for i in range(n):
	for j in range(n):
	  if vis1[i][j]:
	    color = li[i][j]
	    bfs(i, j, color)
	    c2 += 1
print(c1,c2)#  제출 번호 : 79748483, 메모리 : 34112, 시간 : 76