import sys
from collections import deque
input = lambda: sys.stdin.readline().rstrip()
t = int(input())
for _ in range(t):
  p = input()
  n = int(input())
  q = deque(input().lstrip('[').rstrip(']').split(','))
  if n==0:q=deque()
  tf=False
  num = 0
  for i in p:
    if i == 'R':
      num+=1
    elif i == "D":
      if len(q) == 0:
        print('error')
        tf=True
        break
      if num%2 == 0:
        q.popleft()
      else:
        q.pop()
  if tf:continue
  else:
    if num%2 != 0:q.reverse()
    print('[', end = '')
    print(*q,sep =',', end = '')
    print(']')#  제출 번호 : 79646706, 메모리 : 42984, 시간 : 276