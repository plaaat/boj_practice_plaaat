import sys
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
nli = list(map(int,input().split()))
nli.sort()
vis = [False]*n
li = []
def dfs():
  tem = -1
  if len(li) == m:
    print(*li)
    return
  for i in range(n):
    if not vis[i] and tem!=nli[i]:
      li.append(nli[i])
      tem = nli[i]
      vis[i] = True
      dfs()
      li.pop()
      vis[i] = False 
dfs()#  ���� ��ȣ : 80049422, �޸� : 31120, �ð� : 76