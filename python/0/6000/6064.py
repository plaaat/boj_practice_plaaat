import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
t = int(input())
for i in range(t):
  m,n,x,y = map(int,input().split())
  tf = True
  tem = x
  while tem<=m*n:
    if (tem-x)%m == 0 and (tem-y)%n ==0:
      print(tem)
      tf = False
      break
    tem+=m
  if tf:print(-1)


#  제출 번호 : 79927306, 메모리 : 34016, 시간 : 4256