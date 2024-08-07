import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
le = {}
sn = {}
for _ in range(n):
  a,b = map(int,input().split())
  le[a] = b
for _ in range(m):
  a,b = map(int,input().split())
  sn[a] = b
vis = [False]*101
nums = [0]*101

def bfs():
  q = deque([1])
  while q:
    x = q.popleft()
    if x == 100:
      print(nums[-1])
      break
    else:
      for i in range(6):
        tem = x+i+1
        if tem<=100 and not vis[tem]:
          if tem in le:
            tem = le[tem]
          if tem in sn:
            tem = sn[tem]
          if not vis[tem]:
            vis[tem] = True
            nums[tem]+=nums[x]+1
            q.append(tem)
bfs()


#  제출 번호 : 79773678, 메모리 : 34052, 시간 : 64