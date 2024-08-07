import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
a,b,c = map(int,input().split())
li = [list(map(int,input().split())) for _ in range(n)]
d = [(-1,0),(0,1),(1,0),(0,-1)]
li[a][b]+=2
num = 1
while True:
  tf = True
  if c<0:
    c+=4
  for i in range(4):
    c-=1
    x,y = a+d[c][0],b+d[c][1]
    if 0<=x<n and 0<=y<m and li[x][y] == 0:
      num+=1
      li[x][y]+=2
      a,b = x,y
      tf = False
      break
  if tf:
    if li[a-d[c][0]][b-d[c][1]] == 1:
      print(num)
      break
    else:
      a,b = a-d[c][0],b-d[c][1]


#  제출 번호 : 79646138, 메모리 : 34072, 시간 : 64