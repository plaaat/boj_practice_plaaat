import sys
input = lambda:sys.stdin.readline().rstrip()

n,m = map(int,input().split())
nli = list(map(int,input().split()))
nli.sort()
li = []
def dfs(x):
  tem = -1
  if len(li) == m:
    print(*li)
    return
  for i in range(x-1,n):
    if tem!=nli[i]:
      li.append(nli[i])
      tem = nli[i]
      dfs(i+1)
      li.pop() 
dfs(1)


#  제출 번호 : 80049725, 메모리 : 31120, 시간 : 52