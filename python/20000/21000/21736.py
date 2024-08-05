import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = []
for i in range(n):
  tl = list(input())
  if "I" in tl:
    y = i
    x = tl.index('I')
  li.append(tl)
d = [(1,0),(0,1),(-1,0),(0,-1)]
vis = [[False]*m for _ in range(n)]
def bfs(a,b):
  num = 0
  q = deque([[a,b]])
  while q:
    dx,dy = q.popleft()
    for i in d:
      x,y = dx+i[0],dy+i[1]
      if 0<=x<m and 0<=y<n and not vis[y][x]:
        vis[y][x] = True
        if li[y][x] != "X":
          q.append([x,y])
          if li[y][x] == "P":
            num+=1
  if num == 0:
    print('TT')
  else:
    print(num)

bfs(x,y)#  제출 번호 : 79774158, 메모리 : 40484, 시간 : 308