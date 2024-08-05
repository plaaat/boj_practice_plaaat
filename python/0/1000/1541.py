import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n = input()
mn = n.split('-')
pn = 0
if n[0] == '-':
  pn -= sum(map(int,mn[0].split('+')))
else:
  pn += sum(map(int,mn[0].split('+')))
for i in mn[1:]:
  i = sum(map(int,i.split('+')))
  pn -= i
print(pn)#  제출 번호 : 79900239, 메모리 : 34016, 시간 : 60