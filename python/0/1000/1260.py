import sys
from collections import deque
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

n,m,v = map(int,input().split())
li = [[0]*(n+1) for _ in range(n+1)]
for _ in range(m):
  a,b = map(int,input().split())
  li[a][b] = 1
  li[b][a] = 1
visd = [True]*(n+1)
visb = [True]*(n+1)
pd = []
pb = []
def dfs(v):
  visd[v] = False
  pd.append(v)
  for i in range(1,n+1):
    if li[v][i] == 1 and visd[i]:
      dfs(i)

def bfs(v):
  q = deque([v])
  visb[v] = False
  while q:
    v = q.popleft()
    pb.append(v)
    for i in range(1,n+1):
      if li[v][i] == 1 and visb[i]:
        q.append(i)
        visb[i] = False
dfs(v)
bfs(v)
print(*pd)
print(*pb)


#  제출 번호 : 79686275, 메모리 : 39616, 시간 : 172