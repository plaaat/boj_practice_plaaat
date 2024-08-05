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
    dfs(i)
    li.pop()
dfs(1)#  제출 번호 : 79970594, 메모리 : 34016, 시간 : 100