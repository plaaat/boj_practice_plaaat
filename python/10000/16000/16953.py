import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
q = deque([[n,1]])
vis = set()
tf = True
while q:
  a,b = q.popleft()
  if a == m:
    print(b)
    tf = False
    break
  sa = int(str(a)+"1")
  if sa <= m and not sa in vis:
    q.append([sa,b+1])
    vis.add(sa)
  if a*2 <= m and not a*2 in vis:
    q.append([a*2,b+1])
    vis.add(a*2)
if tf:print(-1)


#  제출 번호 : 79855686, 메모리 : 37352, 시간 : 140