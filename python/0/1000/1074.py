import sys
sys.setrecursionlimit(10**7)
input = lambda: sys.stdin.readline().rstrip()

n,r,c = map(int,input().split())
num = 0

while n!=0:
  n-=1
  if r < 2 ** n and c < 2 ** n:
    continue
  elif r < 2**n and c >= 2**n: 
    num += ( 2 ** n) * ( 2 ** n )
    c -= ( 2 ** n )
  elif r >= 2 ** n and c < 2 ** n:
    num += ( 2 ** n ) * ( 2 ** n ) * 2
    r -= ( 2 ** n )
  else:
	  num += ( 2 ** n ) * ( 2 ** n ) * 3
	  r -= ( 2 ** n )
	  c -= ( 2 ** n )
print(num)#  제출 번호 : 79646734, 메모리 : 31120, 시간 : 44