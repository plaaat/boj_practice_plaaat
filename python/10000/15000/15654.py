import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = list(map(int,input().split()))
li.sort()
pli = []
def dfs(x):
  if len(pli) == m:
    print(*pli)
    return
  for i in range(n):
    if li[i] in pli:
      continue
    pli.append(li[i])
    dfs(i)
    pli.pop()
dfs(0)#  ���� ��ȣ : 80000232, �޸� : 34016, �ð� : 232