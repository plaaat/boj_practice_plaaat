import sys
from collections import deque
n = int(input())
li = [list(map(int,input())) for i in range(n)]
d = [(0,1),(0,-1),(1,0),(-1,0)]
pl = []
def bfs(a,b):
  q = deque([(a,b)])
  num = 0
  while q:
    x,y = q.popleft()
    for i in d:
      xx = x+i[0]
      yy = y+i[1]
      if -1<xx<=n-1 and -1<yy<=n-1 and li[xx][yy] != 0:
          q.append([xx,yy])
          li[xx][yy] -= 1
          num+=1
  if num == 0:
    pl.append(1)
  else:pl.append(num)  
for i in range(n):
  for s in range(n):
    if li[i][s] == 1:
      bfs(i,s)
print(len(pl))
pl.sort()
print(*pl, sep = '\n')#  제출 번호 : 79646611, 메모리 : 34072, 시간 : 64