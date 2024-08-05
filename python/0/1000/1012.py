import sys
sys.setrecursionlimit(9999)
input = lambda: sys.stdin.readline().rstrip()

t = int(input())

def fin(a,b):
  global num
  if a<0 or b<0 or a>= m or b >= n:
    return
  if li[a][b] == 1:
    li[a][b] = 0
    fin(a-1,b)
    fin(a+1,b)
    fin(a,b-1)
    fin(a,b+1)
    return True
  return
for _ in range(t):
  m,n,k = map(int,input().split())
  li = []
  for i in range(m):
    li.append([0]*n)
  for _ in range(k):
    x,y = map(int,input().split())
    li[x][y] = 1
  num = 0
  for i in range(m):
    for s in range(n):
      if fin(i,s):
        num+=1
  print(num)#  제출 번호 : 79646807, 메모리 : 31420, 시간 : 56