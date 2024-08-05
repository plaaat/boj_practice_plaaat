import sys
input = sys.stdin.readline

n = int(input())
a = 0
nl = list(map(int,input().split()))
nl.sort()
n+=1
for i in nl:
  n-=1
  a+=i*n
print(a)#  제출 번호 : 79650094, 메모리 : 31120, 시간 : 44