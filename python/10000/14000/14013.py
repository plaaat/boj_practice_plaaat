import sys
input = lambda:sys.stdin.readline().rstrip()
x,y = map(float,input().split())

for _ in range(int(input())):
  n,a = input().split()
  n = float(n)
  if n == 0:
    print(0)
    continue
  if a == 'A':
    print(y*n/x)
  else:
    print(x*n/y)


#  제출 번호 : 79646460, 메모리 : 31120, 시간 : 284