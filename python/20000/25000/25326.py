import sys
input = lambda:sys.stdin.readline().rstrip()
n,m = map(int,input().split())
li = []
for _ in range(n):
  li.append((input().split()))
for _ in range(m):
  a,b,c = input().split()
  num = 0
  for s,f,d in li:
    if s == a or a == '-':
      if f == b or b == '-':
        if d == c or c =='-':
          num+=1
  print(num)#  제출 번호 : 79646423, 메모리 : 31120, 시간 : 212