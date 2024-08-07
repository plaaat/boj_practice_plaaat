import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = [list(map(int,input().split())) for _ in range(n)]
bl = 0
wh = 0

def find(x,y,n):
  global bl
  global wh
  a = li[x][y]
  for i in range(x,x+n):
    for s in range(y,y+n):
      if li[i][s] != a:
        find(x,y,n//2)
        find(x,y+n//2,n//2)
        find(x+n//2,y,n//2)
        find(x+n//2,y+n//2,n//2)
        return
  if a == 0:
    wh+=1
  else:
    bl+=1
find(0,0,n)
print(wh)
print(bl)


#  제출 번호 : 79646787, 메모리 : 31120, 시간 : 48