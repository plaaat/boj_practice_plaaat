import sys
input = lambda: sys.stdin.readline().rstrip()

n = int(input())
li = [0]*(n+1)

if n == 1:
  print(1)
elif n == 2:
  print(3)
elif n == 3:
  print(5)
else:
  li[1] = 1
  li[2] = 3
  li[3] = 5
  for i in range(4,n+1):
    li[i] = li[i-1]+li[i-2]*2
  print(li[n]%10007)#  제출 번호 : 79649648, 메모리 : 31120, 시간 : 44