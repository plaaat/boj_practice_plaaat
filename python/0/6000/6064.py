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
  if tf:print(-1)#  ���� ��ȣ : 79927306, �޸� : 34016, �ð� : 4256