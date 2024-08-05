import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
pli = [list(map(int,input().split())) for _ in range(n)]
for i in range(n):
  for j in range(n):
    for s in range(n):
      if pli[j][i] == 1 and pli[i][s] == 1:
        pli[j][s] = 1
for i in pli:
  print(*i)#  제출 번호 : 79936795, 메모리 : 34168, 시간 : 240