import sys
input = lambda:sys.stdin.readline().rstrip()
n = int(input())
num = 0
for i in range(n+1):
  num+=i
  for s in range(n+1):
    num+=s
print(num)#  제출 번호 : 79646484, 메모리 : 31120, 시간 : 124