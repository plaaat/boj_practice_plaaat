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
  print(*i)#  ���� ��ȣ : 79936795, �޸� : 34168, �ð� : 240