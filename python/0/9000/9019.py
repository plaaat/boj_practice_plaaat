import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

t = int(input())
def d(n):
  if n*2>9999:return int((2*n)%10000)
  else:return 2*n
def s(n):
  if n ==0:return 9999
  else:return n-1
def l(n):
  return (n%1000)*10+n//1000
def r(n):
  return (n%10)*1000+n//10
for _ in range(t):
  n,m = map(int,input().split())
  q = deque([[n,'?']])
  vis = [False]*10001
  pl = []
  while q:
    a,wo = q.popleft()
    if a == m:
      print(wo.lstrip('?'))
    td = d(a)
    if not vis[td]:
      vis[td] = True
      q.append([td,wo+'D'])
    ts = s(a)
    if not vis[ts]:
      vis[ts] = True
      q.append([ts,wo+'S'])
    tl = l(a)
    if not vis[tl]:
      vis[tl] = True
      q.append([tl,wo+'L'])
    tr = r(a)
    if not vis[tr]:
      vis[tr] = True
      q.append([tr,wo+'R'])


#  제출 번호 : 79828451, 메모리 : 214112, 시간 : 9508