import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

n,m = map(int,input().split())
chli = [0]*(n+1)
li = {}
for i in range(1,n+1):
  li[i] = []
for _ in range(m):
  a,b = map(int,input().split())
  li[a].append(b)
  li[b].append(a)
def fin(n):
  global chli
  chli[n]+=1
  for i in li[n]:
    if chli[i] == 0:
      chli[i]+=1
      fin(i)
num = 0

for i in range(1,n+1):
  if chli[i] == 0:
    num+=1
    fin(i)
print(num)


#  제출 번호 : 79646777, 메모리 : 65032, 시간 : 636