import sys
input=lambda:sys.stdin.readline().rstrip()

n,m = map(int, input().split())
a = 0
li = tuple(map(int,input().split()))
pl = [0]
for i in li:
  a+=i
  pl.append(a)
for _ in range(n):
  try:
    i,j = map(int,input().split())
    print(pl[j]-pl[i-1])
  except:
    break#  제출 번호 : 79650012, 메모리 : 41240, 시간 : 280