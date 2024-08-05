import sys
from collections import deque
input = lambda:sys.stdin.readline()

n = int(input())
t = int(input())
wo = input()
pn = 0
c = 0
tem = 0
while c<(t-1):
  if wo[c:c+3] == 'IOI':
    tem+=1
    c+=2
    if tem == n:
      pn+=1
      tem -= 1
  else:
    c+=1
    tem = 0
print(pn)#  제출 번호 : 79901559, 메모리 : 34212, 시간 : 372