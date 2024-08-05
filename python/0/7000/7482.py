import sys

input = lambda: sys.stdin.readline().rstrip()

n = int(input())

for _ in range(n):

  m = round(float(input())/6 ,10)+0.00000000001

  print(str(m)[0:-1])#  제출 번호 : 79641401, 메모리 : 31120, 시간 : 44