import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = [list(map(int,input())) for _ in range(n)]
d = [(1,0),(-1,0),(0,1),(0,-1)]
def bfs():
  q = deque([(0,0)])
  while q:
    x,y = q.popleft()
    for i in range(4):
      nx, ny = x+d[i][1], y+d[i][0]
      if 0<=nx<n and 0<=ny<m:
        if li[nx][ny] == 1:
          q.append((nx,ny))
          li[nx][ny] = li[x][y]+1
bfs()
print(li[-1][-1])


#  제출 번호 : 79686379, 메모리 : 34184, 시간 : 72