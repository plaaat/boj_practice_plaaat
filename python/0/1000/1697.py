import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
num = 100000
visit = [0]*100001
q = deque()
q.append(n)
while q:
  t = q.popleft()
  if t == m:
    print(visit[t])
    break
  else:
    if 0<=t-1<=num and not visit[t-1]:
      visit[t-1] = visit[t]+1
      q.append(t-1)
    if 0<=t+1<=num and not visit[t+1]:
      visit[t+1] = visit[t]+1
      q.append(t+1)
    if 0<=t*2<=num and not visit[t*2]:
      visit[t*2] = visit[t]+1
      q.append(t*2)#  제출 번호 : 79646751, 메모리 : 35300, 시간 : 156