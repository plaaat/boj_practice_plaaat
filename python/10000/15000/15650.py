import sys
from collections import deque
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
li = []
def dfs(x):
  if len(li) == m:
    print(*li)
    return
  for i in range(x,n+1):
    li.append(i)
    dfs(i+1)
    li.pop()
dfs(1)#  ���� ��ȣ : 79885057, �޸� : 34016, �ð� : 100