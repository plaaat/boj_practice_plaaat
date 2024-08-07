import sys
from collections import deque
import heapq
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
  n = int(input())
  q = []
  mq = []
  di = {}
  num = 0
  for _ in range(n):
    a,b = input().split()
    b = int(b)
    if a == 'I':
      num+=1
      if b in di:
        di[b]+=1
      else:
        di[b] = 1
        heapq.heappush(q,b)
        heapq.heappush(mq,-b)
    else:
      if b == 1 and num>0:
        while -mq[0] not in di or di[-mq[0]] < 1:
          t = -heapq.heappop(mq)
          if t in di:
            del(di[t])
        di[-mq[0]] -= 1
        num-=1
      elif b == -1 and num>0:
        while q[0] not in di or di[q[0]] < 1:
          t = heapq.heappop(q)
          if t in di:
            del di[t]
        di[q[0]] -= 1
        num-=1
  if num == 0:
    print('EMPTY')
  else:
    while -mq[0] not in di or di[-mq[0]] < 1:
      heapq.heappop(mq)
    while q[0] not in di or di[q[0]] < 1:
      heapq.heappop(q)
    print(-mq[0], q[0])


#  제출 번호 : 79646636, 메모리 : 178856, 시간 : 5492