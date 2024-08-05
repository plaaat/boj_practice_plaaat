import sys
input=lambda:sys.stdin.readline().rstrip()

def fibo(n):
    global memo
    global li
    if n in memo:
      li[n+2] = (li[n+1][0]+li[n][0],li[n+1][1]+li[n][1])
      return memo[n]
    if n == 0:
        memo[0] = 0
        li[0] = (1,0)
        return 0
    elif n == 1:
        memo[1] = 1
        li[1] = (0,1)
        return 1
    else:
      memo[n] = fibo(n-1) + fibo(n-2)
      return memo[n]

for i in range(int(input())):
  memo = {}
  li = {2:(1,1)}
  n = int(input())
  fibo(n)
  print(*li[n])#  제출 번호 : 79649954, 메모리 : 31120, 시간 : 40